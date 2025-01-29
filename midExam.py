class Star_Cinema:
    hall_list=[]

    @classmethod
    def entry_hall(cls,hall):
        if isinstance(hall,Hall):
            cls.hall_list.append(hall)
        else:
            raise ValueError("Only excepts the instance of Hall class.")

# Hall class
class Hall:
    def __init__(self,rows,cols,hall_no):
        self._seats={}
        self._show_list=[]
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no

        Star_Cinema.entry_hall(self)

    # entry show method
    def entry_show(self,id,movie_name,time):
        show=(id,movie_name,time)
        self._show_list.append(show)
        # reset the seat 
        self._seats[id]=[[False for _ in range (self._cols)]for _ in range (self._rows)]
    
    # book seat method
    # def book_seats(self,id,seat_list):
    #     if id not in self._seats:
    #         raise ValueError("Show ID is invalid")
    #     for row,col in seat_list:
    #         if row<0 or col<0 or row>=self._rows or col>=self._cols:
    #         # if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
    #             raise ValueError(f"Invalid seat : row-> {row} col->{col}.")
    #         elif self._seats[id][row][col]:
    #             raise ValueError(f"This seat is already booked  row-> {row} col->{col}.")
    #         else:
    #             self._seats[id][row][col]=True
    def book_seats(self, id, seat_list):
        if id not in self._seats:
            raise ValueError("Invalid show ID.")

        for row, col in seat_list:
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                raise ValueError(f"Invalid seat: ({row}, {col}).")
            if self._seats[id][row][col]:
                raise ValueError(f"Seat ({row}, {col}) is already booked.")
            self._seats[id][row][col] = True
            

    # view show list method
    def view_show_list(self):
        print("Show is running in this hall : ")
        for show in self._show_list:
            print(f"{show[0]} Movie name : {show[1]} Show time : {show[2]}")
        # for show in self._show_list:
        #     print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
            # print(show)

    def getShowList(self):
        return self._show_list
    # view available seats
    def view_available_seats(self,id):
        if id not in self._seats:
            raise ValueError("Invalid show ID")
        
        print(f" Available seat for show {id}")
        for r in range (self._rows):
            for c in range (self._cols):
                if not self._seats[id][r][c]:
                    print(f'Row -> {r} Col -> {c}')

# main replica function
def main():
    hall1=Hall(rows=5,cols=5,hall_no=1)
    hall1.entry_show("s1","Inception","10:00 AM")
    hall1.entry_show("s2","Conqure of Osman","2:00 PM")
    while True:
        print("\nWelcome to Star_Cinema!!")
        print("1. View All Shows")
        print("2. View Available Seats")
        print("3. Book Seats")
        print("4. Exit")
        
        choice=int(input("Enter your choice : "))
        if choice==1:
            try:
                hall1.view_show_list()
            except ValueError as e:
                print(e)
        elif choice==2:
            show_id=input("Enter the show id : ")
            try:
                hall1.view_available_seats(show_id)
            except ValueError as err:
                print(err)
        elif choice==3:
           
            show_id = input("Enter show ID: ")
            seat_list = []
            try:
                num_seats = int(input("How many seats do you want to book? "))
                for _ in range(num_seats):
                    row = int(input("Enter row: "))
                    col = int(input("Enter column: "))
                    seat_list.append((row, col))
                hall1.book_seats(show_id, seat_list)
                print("Seats booked successfully!")
            except ValueError as e:
                print(e)
        elif choice==4:
            print("Thanks for choosing Star Cinema.")
            break
        else:
            print("Invalid Choice try again.")


if __name__ == "__main__":
    main()
    