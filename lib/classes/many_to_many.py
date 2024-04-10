class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        if self not in NationalPark.all:
            NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name'):
            if isinstance(name, str) and len(name)>= 3:
                self._name = name
            else:
                raise TypeError("name must be string and its length must be greater than or equal to 3")
        else:
            raise TypeError("park name is immutable")

        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))
    
    def total_visits(self):
        visits = [trip for trip in Trip.all if trip.national_park == self]
        return len(visits)
    
    def best_visitor(self):
        all_trips_this_park = NationalPark.trips(self)
        most_visit = 0
        best_visitor = None
        for visitor in Visitor.all:
            visits = 0
            for trip in all_trips_this_park:
                if trip.visitor == visitor:
                    visits += 1
            if visits >= most_visit:
                most_visit =  visits
                best_visitor = visitor
        return best_visitor

    @classmethod
    def most_visited(cls):
        highest_visit = 0
        most_visited_park = None
        for park in cls.all:
           if cls.total_visits(park) >= highest_visit:
            highest_visit = cls.total_visits(park)
            most_visited_park = park
        return most_visited_park

        
class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property 
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise TypeError("visitor must be a Visitor class")

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise TypeError("national_park must be a NationalPark class")
    
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise TypeError("start_date format is not correct")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        else:
            raise TypeError("end_date format is not correct")


class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        if self not in Visitor.all:
            Visitor.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            if len(name) >= 1 and len(name) <= 15:
                self._name = name
            else:
                raise TypeError("the name lenght is between 1 and 15")
        else:
            raise TypeError("name must be a string")

        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in Trip.all if trip.visitor == self]))
    
    def total_visits_at_park(self, park):
        all_trips = Visitor.trips(self)
        this_park_visit = []
        for trip in all_trips:
            if trip.national_park == park:
                this_park_visit.append(trip)
        return len(this_park_visit)


