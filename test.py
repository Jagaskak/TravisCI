def try_assert():
    assert(1 + 1 == 1)
 
def dont_assert():
    assert(1 + 1 == 2)
    
dont_assert()

try:
    try_assert()
except:
    # Supposed to fail, so don't do anything
    pass
    
