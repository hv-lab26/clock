import time
import math
import os
import sys
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class SimpleASCIIClock:
    def __init__(self, radius=15):
        self.radius = radius
        self.center_x = radius
        self.center_y = radius
        self.size = radius * 2 + 1
        
    def draw_clock(self):
        now = datetime.now()
        hours = now.hour % 12
        minutes = now.minute
        seconds = now.second
        
        hour_angle = (hours * 30 + minutes * 0.5) * math.pi / 180
        minute_angle = minutes * 6 * math.pi / 180
        second_angle = seconds * 6 * math.pi / 180
        
        clock = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        
        for angle in range(0, 360, 3):
            rad = angle * math.pi / 180
            x = round(self.center_x + self.radius * math.cos(rad))
            y = round(self.center_y + self.radius * math.sin(rad))
            if 0 <= x < self.size and 0 <= y < self.size:
                clock[y][x] = 'o'
        
        numbers = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        for i in range(12):
            angle = (i * 30 - 90) * math.pi / 180
            x = round(self.center_x + (self.radius - 3) * math.cos(angle))
            y = round(self.center_y + (self.radius - 3) * math.sin(angle))
            if 0 <= x < self.size and 0 <= y < self.size:
                num = numbers[i]
                if len(num) == 1:
                    clock[y][x] = num
                else:
                    if x > 0:
                        clock[y][x-1] = num[0]
                    if x < self.size - 1:
                        clock[y][x] = num[1]
        
        second_length = int(self.radius * 0.9)
        dx = math.cos(second_angle - math.pi/2)
        dy = math.sin(second_angle - math.pi/2)
        for i in range(second_length + 1):
            x = round(self.center_x + i * dx)
            y = round(self.center_y + i * dy)
            if 0 <= x < self.size and 0 <= y < self.size:
                clock[y][x] = '@'
        
        minute_length = int(self.radius * 0.75)
        dx = math.cos(minute_angle - math.pi/2)
        dy = math.sin(minute_angle - math.pi/2)
        for i in range(minute_length + 1):
            x = round(self.center_x + i * dx)
            y = round(self.center_y + i * dy)
            if 0 <= x < self.size and 0 <= y < self.size:
                clock[y][x] = '$'
        
        hour_length = int(self.radius * 0.5)
        dx = math.cos(hour_angle - math.pi/2)
        dy = math.sin(hour_angle - math.pi/2)
        for i in range(hour_length + 1):
            x = round(self.center_x + i * dx)
            y = round(self.center_y + i * dy)
            if 0 <= x < self.size and 0 <= y < self.size:
                clock[y][x] = '#'
        
        clock[self.center_y][self.center_x] = '*'
        
        return '\n'.join(''.join(row) for row in clock)

def main():
    clock = SimpleASCIIClock(radius=12)
    
    print("2D ASCII CLOCK - Press Ctrl+C to exit")
    print("Hour hand: #  |  Minute hand: $  |  Second hand: @")
    print("=" * 50)
    
    try:
        while True:
            clear_screen()
            
            now = datetime.now()
            
            day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                          'July', 'August', 'September', 'October', 'November', 'December']
            
            day_name = day_names[now.weekday()]
            month_name = month_names[now.month - 1]
            
            print(f"Time: {now.strftime('%I:%M:%S %p')}")
            print(f"Date: {day_name}, {month_name} {now.day}, {now.year}")
            print()
            
            clock_display = clock.draw_clock()
            print(clock_display)
            print()
            print("Hour hand: #  |  Minute hand: $  |  Second hand: @")
            print("Press Ctrl+C to exit")
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nClock terminated!")
        sys.exit(0)

if __name__ == "__main__":
    main()