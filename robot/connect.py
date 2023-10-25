#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script demonstrates how to retrieve data from a V3SCamera device. It
does not depend on the V3SCamera API, but the functionality is comparable.
Please have a look at the samples point cloud conversion examples in order
to get more elaborate examples (e.g. how to transform distance values into
a 3D point cloud).

Author: GBC09 / BU05 / SW
SICK AG, Waldkirch
email: techsupport0905@sick.de

Copyright note: Redistribution and use in source, with or without modification, are permitted.

Liability clause: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""




#image output from camera:
#image output from 3D sensor: 512x424px

import argparse
import socket
import struct
import traceback
import csv

from common.Control import Control
from common.Streaming import Data
from common.Stream import Streaming
from common.Streaming.BlobServerConfiguration import BlobClientConfig

import cv2
import os
import numpy


# coding: utf-8
# tcp stream server
import socket
import logging
import time
import datetime as dt
from threading import Thread, currentThread

from random import randint, choice

import random


directory = r'C:/Users/Wrigh/Desktop/New folder/Python/Images'
# Change the current directory
# to specified directory
os.chdir(directory)

# configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(process)s %(threadName)s |%(message)s",
)



class Server:

    def __init__(self, host='172.16.1.241', port=8099):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind((host, port))
        self.msg = None

    def read(self, conn: socket.socket = None):

        while True:
            try:
                data = conn.recv(1024).decode()
            except Exception as e:
                logging.info("recv failed: %s", e)
                return
            logging.info("[R %s]<< %s message from ABB", currentThread().getName(), data)
            self.msg = data
            time.sleep(1)

    def write(self, conn: socket.socket = None,):

        while True:
            #rand = randint(0, 1)
            content=str(3)
            print(content)
            #msg = r""# int(dt.datetime.now())/2 #int(f"{dt.datetime.now()} - {self.msg}")/2
            msg = content.encode("utf-8")
            logging.info("[W %s]>> %s Command to ABB", currentThread().getName(), msg)
            try:
                conn.send(msg)#(msg.encode())
            except Exception as e:
                logging.info("send failed: %s", e)
                return
            time.sleep(1)

    def serve(self):
        """ Start service """
        self._sock.listen()
        logging.info("Serving...")
        while True:
            logging.info("Waiting for connection...")
            conn, addr = self._sock.accept()
            logging.info("Recived new conn: %s from %s", conn, addr)
            # Start IO for this connection
            Thread(target=self.read, args=(conn, )).start()
            Thread(target=self.write, args=(conn, )).start()
            time.sleep(1)
            #Thread(target=self.write(databit=0), args=(conn, )).start()


class Connect:
    def __init__(self):
        pass

    def start_session(self):
        # === Device specific protocol & control_port mapping ===
        # Visionary-T CX / AG / DT => CoLaB / Port 2112
        # Visionary-S CX           => CoLaB / Port 2112
        # Visionary-T Mini CX      => CoLa2 / Port 2122
        parser = argparse.ArgumentParser(description="Exemplary data reception from SICK Visionary devices.")
        parser.add_argument('-i', '--ipAddress', required=False, type=str,
                            default="192.168.136.3", help="The ip address of the device.")
        parser.add_argument('-r', '--ipAddressReceiver', required=False, type=str,
                            default="192.168.1.2", help="The ip address of the receiving PC (UDP only).")
        parser.add_argument('-p', '--protocol', required=False, choices=['ColaB', 'Cola2'],
                            default="Cola2", help="The SICK Cola protocol version.")
        parser.add_argument('-c', '--control_port', required=False, type=int,
                            default=2122, help="The control port to change settings.")
        parser.add_argument('-s', '--streaming_port', required=False, type=int,
                            default=2114, help="The tcp port of the data channel.")
        parser.add_argument('-t', '--transport_protocol', required=False, choices=['TCP', 'UDP'],
                            default="TCP", help="The transport protocol.")
        args = parser.parse_args()

        # create and open a control connection to the device
        deviceControl = Control(args.ipAddress, args.protocol, args.control_port)
        deviceControl.open()

        # access the device via a set account to change settings
        deviceControl.login(Control.USERLEVEL_SERVICE, 'CUST_SERV')

        name, version = deviceControl.getIdent()

        disableDMDataTransferInCleanup = False
        if " AG " in name.decode('utf-8'):
            # Depth map data transfer is enabled if no data transfer (with corresponding data reduction)
            # was enabled on the device. Otherwise the AG device wouldn't stream any data.
            if not (deviceControl.getDepthMapDataTransfer()
                    or (deviceControl.getPolarDataTransfer() and deviceControl.getPolarReduction())
                    or (deviceControl.getCartesianDataTransfer() and deviceControl.getCartesianReduction())):
                disableDMDataTransferInCleanup = True
                deviceControl.enableDepthMapDataTransfer()

        # streaming settings:
        streamingSettings = BlobClientConfig()
        streaming_device = None

        # configure the data stream
        #   the methods immediately write the setting to the device
        if args.transport_protocol == "TCP":
            # set protocol and device port
            streamingSettings.setTransportProtocol(deviceControl, streamingSettings.PROTOCOL_TCP)
            streamingSettings.setBlobTcpPort(deviceControl, args.streaming_port)
            # start streaming
            streaming_device = Streaming(args.ipAddress, args.streaming_port)
            streaming_device.openStream()

        elif args.transport_protocol == "UDP":
            # settings
            streamingSettings.setTransportProtocol(deviceControl, streamingSettings.PROTOCOL_UDP)  # UDP
            streamingSettings.setBlobUdpReceiverPort(deviceControl, args.streaming_port)
            streamingSettings.setBlobUdpReceiverIP(deviceControl, args.ipAddressReceiver)
            streamingSettings.setBlobUdpControlPort(deviceControl, args.streaming_port)
            streamingSettings.setBlobUdpMaxPacketSize(deviceControl, 1024)
            streamingSettings.setBlobUdpIdleTimeBetweenPackets(deviceControl, 10)  # in milliseconds
            streamingSettings.setBlobUdpHeartbeatInterval(deviceControl, 0)
            streamingSettings.setBlobUdpHeaderEnabled(deviceControl, True)
            streamingSettings.setBlobUdpFecEnabled(deviceControl, False)  # forward error correction
            streamingSettings.setBlobUdpAutoTransmit(deviceControl, True)
            # open the datagram socket
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Bind the socket to the port
            server_address = (
            args.ipAddressReceiver, args.streaming_port)  # use empty hostname to listen on all adapters
            udp_socket.bind(server_address)

            udp_socket.settimeout(1)  # 1sec
            udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4 * 1024 * 1024)  # 4 Megabyte of buffer size

        # logout after settings have been done
        deviceControl.logout()
        deviceControl.startStream()

        myData = Data.Data()

        import time

        try:
            while True:
                if args.transport_protocol == "TCP":
                    streaming_device.getFrame()
                    wholeFrame = streaming_device.frame

                    myData.read(wholeFrame)

                    if __name__ == '__main__':
                        s = Server()
                        s.serve()

                for i in range(0, 360):
                    if myData.hasDepthMap:
                        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
                        up_width = 512
                        up_height = 424
                        up_points = (up_width, up_height)

                        # Check if the webcam is opened correctly
                        if not cap.isOpened():
                            raise IOError("Cannot open webcam")

                        ret, frame = cap.read()
                        frame = cv2.resize(frame, None, fx=0.80, fy=0.883, interpolation=cv2.INTER_AREA)
                        cv2.imshow('Input', frame)
                        name = str("Image" + "%d" + ".jpg") % i
                        cv2.imwrite(name, frame)

                        c = cv2.waitKey(1)

                        distanceData = list(myData.depthmap.distance)
                        arr = numpy.array(distanceData)
                        lidarsize = numpy.shape(arr)
                        print(lidarsize)
                        brr = numpy.reshape(arr, (424, 512))
                        brr = cv2.inRange(brr, 200, 400)
                        bname = str("brr" + "%d" + ".jpg") % i
                        # cv2.imwrite(bname, brr)
                        wrr = numpy.stack((brr,) * 3, axis=-1)
                        drr = brr
                        cv2.imshow("crr", drr)

                        cv2.imwrite("brr.jpg", drr)
                        crr = cv2.imread('brr.jpg')

                        print(numpy.shape(wrr))
                        print(numpy.shape(frame))
                        trr = cv2.cvtColor(crr, cv2.COLOR_BGR2GRAY)
                        print(drr)

                        time.sleep(5)
                        _, err = cv2.threshold(trr, 100, 255, cv2.THRESH_BINARY_INV)
                        contours, hierarchy = cv2.findContours(err, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
                        cv2.imshow("err", err)
                        c = cv2.waitKey(1000)
                        cv2.drawContours(err, contours, -1, (0, 255, 0), 1)
                        # cv2.imshow("err", err)

                        # recordcontours = open("contour%d.txt" %i, "w+")
                        with open('data%d.csv' % i, mode='w', newline='') as file:
                            for contour in contours:
                                res = []
                                for j in contour:
                                    res.append(j)
                                res.append('#')
                                writer = csv.writer(file)
                                writer.writerows(res)

                        # recordcontours.close()

                        cap.release()
                        cv2.destroyAllWindows()

                        time.sleep(1)
                        print(i)

                        # for c in range(len(contours)):
                        #    n_contour = contours[c]
                        #    for d in range(len(n_contour)):
                        #        XY_Coordinates = n_contour[d]
                        #       print(XY_Coordinates)

                # break #uncomment if only one frame should be received
        except KeyboardInterrupt:
            print("")
            print("Terminating")
        except Exception as e:
            print(f"Exception -{e.args[0]}- occurred, check your device configuration")
            print(traceback.format_exc())

        deviceControl.login(Control.USERLEVEL_AUTH_CLIENT, 'CLIENT')
        if args.transport_protocol == "TCP":
            streaming_device.closeStream()
        elif args.transport_protocol == "UDP":
            udp_socket.close()
            # restoring back to TCP mode
            streamingSettings.setTransportProtocol(deviceControl, streamingSettings.PROTOCOL_TCP)
            streamingSettings.setBlobTcpPort(deviceControl, args.streaming_port)

        if disableDMDataTransferInCleanup:
            deviceControl.disableDepthMapDataTransfer()
        deviceControl.logout()

