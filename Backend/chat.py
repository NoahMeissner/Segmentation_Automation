from Backend.LLM import LLM


# questions which the user inputs
ls = ["""Hello! We are going to help you label your object. We need you to answer a few simple questions. 
        Are you ready to begin?""",
      """What type of object is it? (e.g. sweater, pencil case)""",
      """Which color is the object? (e.g. blue)""",
      """What material is the object made of? (e.g. wood)""",
      """What size is the object? (e.g. small, medium, large)""",
      """Is this information correct: type: ${type} , color: ${color}, material: ${material}, size: ${size}?""",
      """Great! You may close the chatbot now. Your object already exists in the database, so there no need
       to run the model.""",
      """Great! You may close the chatbot now. We ran the model, and now the object has been added to the database."""]

def ask_question (list, answer):
    if len(list) == 3:
        question = list[0]\
            .replace('${type}',answer[0])\
            .replace('${color}',answer[1])\
            .replace('${material}',answer[2])\
            .replace('${size}',answer[3])
        set_answer = input(question+'\n')
        if set_answer == 'true':
            return answer
        else:
            return ask_question(ls, [])

    else:
        set_answer = input(list[0]+'\n')
        if set_answer != 'yes':
            answer.append(set_answer)
        list = list[1:]
        return ask_question(list, answer)
        

def assign_size(size):
    # default method in case the chatbot is not working properly
    """
    :param type: type of object
    :return: size in meters
    """
    if size == "small":
        return .1
    elif size == "medium":
        return .2
    elif size == "large":
        return .3

dict_color = {
    'blue': (255, 0, 0),
    'green': (0, 255, 0),
    'red': (0, 0, 255)
}

def assign_color(color_as_String):
    # default method in case the colors are simple
    """
    :param color_as_String: color in string
    :return: color in BGR format
    """
    return dict_color(color_as_String)

if __name__ == "__main__":
    object_LLM = LLM(tuple((ask_question(ls, []))))
    answer = object_LLM.getanswer()