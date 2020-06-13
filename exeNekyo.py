from nekyo import *


################################################################
# 実行ブロック
################################################################
def prompt(obj):
    """
    :param obj　返答するオブジェクト:
    :return　返答内容:
    """

    return obj.get_name() + ':' + obj.get_responder_name() + '> '


print('nobrainNekyo')

nekyo = Nekyo('nekyo')

while True:
    inputs = input(' > ')
    if not inputs:
        print('バイバイ')
        break
    response = nekyo.dialogue(inputs)
    print(prompt(nekyo), response)
