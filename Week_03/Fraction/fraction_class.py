class Fraction:
    def __init__(self, nomerator, denominator):
        self.nomerator = nomerator
        self.denominator = denominator

    def is_prime(self, x):
        if x < 1:
            return False
        for n in range(2, (x)-1):
            if x % n == 0:
                return False
        return True

    def simplify_fraction(self, nomerator, denominator):
        if nomerator == denominator:
            return (1)
        if nomerator != denominator and (self.is_prime(nomerator) and self.is_prime(denominator)):
            return fraction
        bigger_devisor = 2
        for i in range(2, denominator+1):
            if nomerator % i == 0 and denominator % i == 0:
                if i > bigger_devisor:
                    bigger_devisor = i
        return(nomerator//bigger_devisor, denominator//bigger_devisor)

    def __str__(self):
        return "{0} / {1}".format(self.nomerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        sd = self.denominator
        od = other.denominator
        sn = self.nomerator
        on = other.nomerator
        if(sd != od):
            nomer_result = (sn*od) + (on*sd)
            denom_result = sd*od
            return self.simplify_fraction(nomer_result, denom_result)
        else:
            return self.simplify_fraction((sn + on), sd)

    def __sub__(self, other):
        sd = self.denominator
        od = other.denominator
        sn = self.nomerator
        on = other.nomerator
        if(sd != od):
            nomer_result = (sn*od) - (on*sd)
            denom_result = sd*od
            return self.simplify_fraction(nomer_result, denom_result)
        else:
            return self.simplify_fraction((sn - on), sd)


    def __eq__(self, other):
        pass

    def __mul__(self, other):
        pass
