
def convert(st, option):
    result = ''
    sp = st.split('-')
    if option == 1:
        result = '%s년%s월%s일' % (sp[0], sp[1], sp[2])
    elif option == 2:
        result = '%s월%s일%s년' % (sp[1], sp[2], sp[0])
    elif option == 3:
        result = '%s일%s월%s년' % (sp[2], sp[1], sp[0])
    return result

st1 = '2021-05-24'

print(convert(st1,3))