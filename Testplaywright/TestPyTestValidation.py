import pytest 

@pytest.fixture
def preWork(scope="module"):
    print("I setup browser instance")
    return "fail"

@pytest.fixture(scope="function")
def secondWork():
    print("I setup module instance")
    yield 
    print("teas down validation")

def test_initialCheck(preWork,secondWork):
    print("This is first test")
    assert preWork == "fail"


@pytest.mark.skip #run aagum podhu indha line na skip pannido
def test_SecondCheck(preSetupWork,secondWork):
    print("This is Second test")
