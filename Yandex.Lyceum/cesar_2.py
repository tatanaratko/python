def encrypt_caesar(msg, shift=3):
    if shift == 0:
        return msg
    alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    coded_msg = ''
    shift = shift % len(alpha)  
    for i in range(len(msg)):
        register = msg[i].isupper()
        let_result = ''
        if not msg[i].isalpha(): 
            let_result = msg[i]       
        elif alpha.find(msg[i].lower()) + shift >= len(alpha):
            let_numb = alpha.find(msg[i].lower()) + shift - len(alpha)
            let_result = alpha[let_numb]        
        elif alpha.find(msg[i].lower()) + shift <= 0:
            let_numb = alpha.find(msg[i].lower()) + shift + len(alpha)
            let_result = alpha[let_numb]        
        else:
            new_ord = alpha.find(msg[i].lower()) + shift
            let_result = alpha[new_ord]
        if register:
            let_result = let_result.upper()
        coded_msg += let_result
    return coded_msg


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -shift)
