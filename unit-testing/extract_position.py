def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                if line[-1] == start_index:
                    pos = line[start_index:]
                else:
                    num = ['1','2','3','4','5','6','7','8','9','.']
                    pos = line[start_index:] # from start_index to the end.
                    for i in range(len(pos)):
                        if pos[i] not in num:
                            pos = line[start_index:start_index + i]
                            break
            else:
                pos = None
    return pos

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)

def test_extract_position_empty():
    line = ''
    expected_result = None
    actual_result = extract_position(line)
    assert expected_result == actual_result
    
def test_extract_position_normal_with_text_following():
    line = '|update| the positron location in the particle accelerator is x:21.432 and the particle accelerator is underground'
    expected_result = '21.432'
    actual_result = extract_position(line)
    assert expected_result == actual_result

