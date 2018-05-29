def try_assert():
    assert(1 + 1 == 1)
 
def dont_assert():
    assert(1 + 1 == 2)
    
try:
    try_assert():
except:
    dont_assert()
    return 0
    
