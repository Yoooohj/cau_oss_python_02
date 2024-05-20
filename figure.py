import math

class Line:
    """
    길이를 나타내는 Line 클래스를 정의합니다.
    
    속성:
    __length (int 또는 float): 선의 길이, 기본값은 1입니다.
    
    메소드:
    set_length(length): 선의 길이를 설정합니다.
    get_length(): 선의 길이를 반환합니다.
    """

    def __init__(self, length=1):
        """
        Line 객체를 지정된 길이로 초기화합니다.
        
        매개변수:
        length (int 또는 float): 선의 길이. 기본값은 1입니다.
        """
        self.__length = 1
        self.set_length(length)

    def set_length(self, length):
        """
        선의 길이를 설정합니다. 길이는 양수의 int 또는 float이어야 합니다.
        
        매개변수:
        length (int 또는 float): 선의 길이.
        """
        if isinstance(length, (int, float)) and length > 0:
            self.__length = length

    def get_length(self):
        """
        선의 길이를 반환합니다.
        
        반환값:
        int 또는 float: 선의 길이.
        """
        return self.__length


def area_square(line):
    """
    Line 객체의 길이를 변으로 하는 정사각형의 넓이를 계산합니다.
    
    매개변수:
    line (Line): Line 객체.
    
    반환값:
    float: 정사각형의 넓이, 또는 매개변수가 Line 객체가 아니면 0.
    """
    if isinstance(line, Line):
        length = line.get_length()
        return length * length
    return 0


def area_circle(line):
    """
    Line 객체의 길이를 반지름으로 하는 원의 넓이를 계산합니다.
    
    매개변수:
    line (Line): Line 객체.
    
    반환값:
    float: 원의 넓이, 또는 매개변수가 Line 객체가 아니면 0.
    """
    if isinstance(line, Line):
        radius = line.get_length()
        return math.pi * (radius ** 2)
    return 0


def area_regular_triangle(line):
    """
    Line 객체의 길이를 변으로 하는 정삼각형의 넓이를 계산합니다.
    
    매개변수:
    line (Line): Line 객체.
    
    반환값:
    float: 정삼각형의 넓이, 또는 매개변수가 Line 객체가 아니면 0.
    """
    if isinstance(line, Line):
        length = line.get_length()
        return (math.sqrt(3) / 4) * (length ** 2)
    return 0
