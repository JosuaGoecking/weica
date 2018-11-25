import numpy as np
import matplotlib.pyplot as mp
import datetime
import pickle
import json

class consumption:
#private
    def __init__(self, *args):
        if len(args)!=0 and type(args[0])==dict:
            self.__create_user_data(args[0])
            self.__initialize_consumption()
            self.__initialize_dict()
        self.__d_cal, self.__d_amount = self.__create_dict()
        self.__d_user = self.__read_user_data()
        self.__d_help = self.__get_help()
        self.__get_consumption()
        self.__sum=0
        self.__quiet=False
        if len(args)!=0 and args[0]=="q":
            self.__quiet=True
        if not self.__quiet:
            self.__print_banner()
        
    def __print_banner(self):
        print("---------------------------------------------------------------------------")
        print("                                  weica v2.0")
        print("                          Weight Control Assistant")
        print("                        implemented by Josua Göcking")
        print("                    https://github.com/JosuaGoecking/weica")
        print("---------------------------------------------------------------------------")
        print("\nYour user data:")
        self.print_user_data()
        print("\nYour status:")
        self.print_status()
        if self.__get_date()[4:]==self.__d_user["birthday"][4:]:
            print("\nHappy Birthday!")
            print("In celebration of your special day, why don't you take this one off?")
            print("Don't worry, I won't tell anyone ;).")
            
    def __get_help(self):
        with open('data/help.json') as f:
            d_help=json.load(f)
        return d_help
            
    def __get_date(self):
        now = str(datetime.datetime.now())
        s=now[:4]+now[5:7]+now[8:10]
        return s

    def __date2time(self, date):
        return float(date[:4])+ float(date[4:6])/12 + float(date[6:8])/365
        
    def __read_file(self, file):
        # Open file
        f = open(file, "r")
        # Read and ignore header lines
        header1 = f.readline()
        # Loop over lines and extract variables of interest
        for line in f:
            line = line.strip()
            columns = line.split()
        return columns
    
    def __create_user_data(self, d):
        with open('data/user_data.txt', 'wb') as f:
            pickle.dump(d, f)
        if d["gender"]=="male":
            with open('data/measures.txt', 'w') as fm:
                fm.write("#date\t\tweight[kg]\t\tabdomen[cm]\t\tneck[cm]\n")
                fm.write(self.__get_date()+ "\t\t" + str(self.__date2time(self.__get_date())) + "\t\t"+ str(d["weight"]) + 
                         "\t\t" + str(d["abdomen"])+"\t\t" + str(d["neck"])+"\n")
    
    def __read_user_data(self):
        d_user={}
        with open("data/user_data.txt", "rb") as f:
            d_user=pickle.load(f)
        return d_user
        
    def __get_age(self):
        d=self.__d_user
        bday=self.__date2time(d["birthday"])
        today=self.__date2time(self.__get_date())
        return int(today-bday)
        
    def __get_recipe(self, name):
        try:
            d_rec={}
            with open('data/recipes/'+name+'.txt', 'rb') as f:
                d_rec = pickle.load(f)
            for key in d_rec["Zutaten"]:
                if key not in self.__d_cal:
                    print("Warning: "+key+" is not in the calory dictionary. You need to add it before you can use this recipe.")
            return d_rec
        except FileNotFoundError:
            print("ERROR: data/recipes/"+name+".txt does not exist.")
            return -1
        
    def __initialize_consumption(self):
        self.__consumption={}
        with open('data/tmp_consumption.txt', 'wb') as f:
            pickle.dump(self.__consumption, f)
            
    def __get_consumption(self):
        try:    
            with open('data/tmp_consumption.txt', 'rb') as f:
                self.__consumption=pickle.load(f)
        except FileNotFoundError:
            self.__initialize_consumption()
            
    def __save_temp_consumption(self):
        with open('data/tmp_consumption.txt', 'wb') as f:
                pickle.dump(self.__consumption, f)
                
    def __get_color(self, kcal):
        lot, upt = self.__create_demand()
        range=50
        if self.__d_user["cal_demand"]=="formula":
            range=100
        if kcal < lot:
            return "\033[1;36m"
        elif kcal >= lot and kcal < lot+range:
            return "\033[0;32m"
        elif kcal >=lot+range and kcal <= upt:
            return "\033[0;33m"
        else:
            return "\033[1;31m"

    def __initialize_dict(self):
        cal_dict = {}
        amount_dict = {}
        with open('data/cal_dict.txt', 'wb') as f:
            pickle.dump(cal_dict, f)
            pickle.dump(amount_dict, f)

    def __create_dict(self):
        with open("data/cal_dict.txt", "rb") as f:
            cal_dict = pickle.load(f)
            amount_dict = pickle.load(f)
        return cal_dict, amount_dict

    def __print_dictionary(self):
        print('%-30s %10s %20s' % ('', 'kcal', 'amount'))
        for key in self.__d_cal:
            print('%-30s %10s %20s' % (key, str(self.__d_cal[key]), self.__d_amount[key]))
            
    def __get_Harris_Benedict(self):
        if self.__d_user["gender"]=="male":
            return 66.47+(13.7*self.__d_user["weight"])+(5*self.__d_user["height"])-(6.8*self.__get_age())
        elif self.__d_user["gender"]=="female":
            return 655.1+(9.6*self.__d_user["weight"])+(1.8*self.__d_user["height"])-(4.7*self.__get_age())
            
    def __create_demand(self):
        d=self.__d_user
        lot, upt = 0, 0
        if d["cal_demand"]=="file":
            if d["mode"]=="lose":   
                i=1
                j=2
            elif d["mode"]=="keep":
                i=3
                j=4
            elif d["mode"]=="gain":
                i=5
                j=6
            else:
                print("ERROR: Unknown mode.")
            f = open("data/cal_demand.txt", "r")
            header1 = f.readline()
            low_threshold={}
            upper_threshold={}
            for line in f:
                line = line.strip()
                columns = line.split()
                weight = int(columns[0])
                low_demand = float(columns[i])
                up_demand = float(columns[j])
                low_threshold[weight]=low_demand
                upper_threshold[weight]=up_demand
            lot=low_threshold[d["weight"]]
            upt=upper_threshold[d["weight"]]
        elif d["cal_demand"]=="formula":
            cal_demand=int(d["PAL"]*self.__get_Harris_Benedict())
            if d["mode"]=="lose":
                upt=cal_demand-400
                lot=cal_demand-600
            elif d["mode"]=="keep":
                upt=cal_demand
                lot=cal_demand-200
            elif d["mode"]=="gain":
                upt=cal_demand+600
                lot=cal_demand+400
            else:
                print("ERROR: Unknown mode.")
        return lot, upt
            
    def __save_measures(self, date):
        today = self.__date2time(date)
        entry=self.__read_file('data/measures.txt')[0]
        last_entry=self.__date2time(entry)
        gap=float(7/365)
        d=self.__d_user
        if (today-last_entry>gap):
            with open('data/measures.txt', 'a') as f:
                f.write(date + "\t\t"+ str(self.__date2time(date))+ "\t\t" + str(d["weight"]) + "\t\t" + str(d["abdomen"])
                        + "\t\t" + str(d["neck"])+"\n")
            print("data/measures.txt has been updated.")

#public
            
    def BMI(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['BMI'])
            return 0
        elif len(args)==2:
            weight=args[0]
            height=args[1]
            height=float(height)/100
            return weight/pow(height, 2)
        else:
            print("ERROR: Incorrect amount of arguments. Either choose one argument (help) or two (weight and height).")
    
    def body_fat_percentage(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['body_fat_percentage'])
        elif len(args)==3:
            height=args[0]
            abdomen=args[1]
            neck=args[2]
            return 86.010*np.log10(abdomen-neck)-70.041*np.log10(height)+30.29521038
        else:
            print("ERROR: Incorrect amount of arguments. Either choose one argument (help) or three (height, abdomen and neck).")
    
    def print_user_data(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['print_user_data'])
        else:
            print('%-10s %10s' % ('parameter', 'value'))
            for key in self.__d_user:
                print('%-10s %10s' % (key, self.__d_user[key]))
                
    def print_status(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['print_status'])
        print('%-20s %10s' % ('BMI', "{0:.2f}".format(self.BMI(self.__d_user["weight"], self.__d_user["height"]))))
        print('%-20s %10s' % ('Body fat percentage', "{0:.2f}".format(self.body_fat_percentage(self.__d_user["height"],
        self.__d_user["abdomen"], self.__d_user["neck"]))+"%"))
    
    def change_user_data(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['change_user_data'])
        elif len(args)==2:
            key=args[0]
            value=args[1]
            self.__d_user[key]=value
            with open('data/user_data.txt', 'wb') as f:
                pickle.dump(self.__d_user, f)
            self.__d_user=self.__read_user_data()
        else:
            print("ERROR: Incorrect amount of arguments. Either choose one argument (help) or two (key and value)")
    
    def print_dict(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['print_dict'])
        elif len(args)==0:
            self.__print_dictionary()
        else:
            if len(args)==1 and type(args[0])==list:
                args=args[0]
            print('%-30s %15s %20s' % ('', 'kcal', 'amount'))
            for arg in args:
                print('%-30s %15s %20s' % (arg, str(self.__d_cal[arg]), self.__d_amount[arg]))
    
    def add_dict_entry(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['add_dict_entry'])
        elif len(args)==3:
            food=args[0]
            kcal=args[1]
            amount=args[2]
            exists=0
            for key in self.__d_cal:
                if key==food:
                    exists=1
            if not exists:
                self.__d_cal[food]=kcal
                self.__d_amount[food]=amount
                with open('data/cal_dict.txt', 'wb') as f:
                    pickle.dump(self.__d_cal,f)
                    pickle.dump(self.__d_amount,f)
            else:
                print("ERROR: Entry does already exist.")
        else:
            print("ERROR: Incorrect amount of arguments. Either choose one argument (help) or three (food, kcal and amount)")
        
    def rm_dict_entry(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['rm_dict_entry'])
        elif len(args)==1 and args[0]!="help":
            entry=args[0]
            d_cal={}
            d_amount={}
            for key in self.__d_cal:
                if key!=entry:
                    d_cal[key]=self.__d_cal[key]
                    d_amount[key]=self.__d_amount[key]
            self.__d_cal=d_cal
            self.__d_amount=d_amount
            with open('data/cal_dict.txt', 'wb') as f:
                pickle.dump(self.__d_cal, f)
                pickle.dump(self.__d_amount, f)
        else:
            print("ERROR: Incorrect amount of arguments. Either choose one help or an entry as argument.")
            
    def add_recipe(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['add_recipe'])
        elif len(args)==1 and args[0]!="help":
            meta=args[0]["meta"]
            with open('data/recipes/'+meta["Name"]+'.txt', 'wb') as f:
                pickle.dump(args[0], f)
        else:
            print("ERROR: Incorrect amount of arguments. Either choose one (help) or two (name and recipe dictionary)")
    
    def change_recipe(self, *args):
        change=False
        d_rec={}
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['change_recipe'])
        elif ((len(args)-1)%2==0 and len(args)!=1) or (len(args)==2 and type(args[1])==list):
            name=args[0]
            if type(args[1])==list:
                args[1].insert(0, name)
                args=args[1]
            d_rec=self.__get_recipe(name)
            for i in range(1, len(args), 2):
                d_rec["Zutaten"][args[i+1]]=[args[i], "d.u."]
            change=True
        elif len(args)==2:
            name=args[0]
            d_rec=self.__get_recipe(name)
            d_rec["meta"]["Zubereitung"]=args[1]
            change=True
        if change:
            with open("data/recipes/"+args[0]+".txt", "wb") as f:
                pickle.dump(d_rec, f)
                
    def rm_recipe_entry(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['rm_recipe_entry'])
        elif len(args)==2:
            meta={}
            data={}
            d={"Zutaten":data, "meta":meta}
            name=args[0]
            d_rec=self.__get_recipe(name)
            for key in d_rec["Zutaten"]:
                if key!=args[1]:
                    d["Zutaten"][key]=d_rec["Zutaten"][key]
            for key in d_rec["meta"]:
                if key!=args[1]:
                    d["meta"][key]=d_rec["meta"][key]
            with open('data/recipes/'+name+'.txt', 'wb') as f:
                pickle.dump(d, f)
                
    def print_recipe(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['print_recipe'])
        elif len(args)==1:
            name=args[0]    
            d_rec=self.__get_recipe(name)
            if d_rec!=-1:
                d={}
                print("Für " + str(d_rec["meta"]["Portionen"]) + " Portion(en).")
                print("Zutaten:")
                for key in d_rec["Zutaten"]:
                    print('%-10s %30s' % (str(d_rec["Zutaten"][key][0])+" "+str(d_rec["Zutaten"][key][1]), key))
                    d[key]=d_rec["Zutaten"][key][0]
                print("\nZubereitung:\n"+ d_rec["meta"]["Zubereitung"])
                self.compute_consumption(d)
                print("{0:.2f}".format(self.__sum/d_rec["meta"]["Portionen"])+" kcal/Portion.")
                
    def add_recipe_to_consumption(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['add_recipe_to_consumption'])
        elif (len(args)-1)%2==0 or type(args[1])==list:
            name=args[0]
            port=1
            if len(args)>1 and type(args[1])==list:
                args=args[1]
                args.insert(0, name)
            d_rec=self.__get_recipe(name)
            for i in range(1, len(args), 2):
                if args[i+1]!="Portionen":
                    d_rec["Zutaten"][args[i+1]][0]=args[i]
                else:
                    port=args[i]
            li=[]
            for key in d_rec["Zutaten"]:
                if d_rec["Zutaten"][key][1]!='d.u.':
                    print("ERROR: Other units than the dictionary default units (d.u.) have not yet been implemented for the consumption calculation. Please change recipe units accordingly.")
                    break
                else:
                        li.append((port/d_rec["meta"]["Portionen"])*d_rec["Zutaten"][key][0])
                        li.append(key)
            self.add_consumption(li)
                        
    def print_consumption(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['print_consumption'])
        else:
            for key in self.__consumption:
                if self.__consumption[key]!=0:
                    print('%-10s %25s' % ("{0:.2f}".format(self.__consumption[key]), key))
    
    def add_consumption(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['add_consumption'])
        elif (len(args)%2!=0 or len(args)==0) and type(args[0])!=list:
            print("ERROR: Two arguments needed per entry.")
        else:
            if len(args)==1 and type(args[0])==list:
                args=args[0]
            for i in range(0, len(args), 2):
                if args[i+1] in self.__consumption:
                    self.change_consumption_entry(args[i+1], args[i], "add", "q")
                else:
                    self.__consumption[args[i+1]]= args[i]
            self.__save_temp_consumption()
            self.compute_consumption()
        
    def rm_consumption_entry(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['rm_consumption_entry'])
        elif len(args)==1 and args[0]=="all":
            self.__consumption={}
        else:
            d={}
            entry = args[0]
            for i in self.__consumption:
                if i!=entry:
                    d[i] = self.__consumption[i]
            self.__consumption=d
            self.compute_consumption()
        self.__save_temp_consumption()
        
    def change_consumption_entry(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['change_consumption_entry'])
        elif len(args)>=3:
            quiet=False
            if len(args)==4 and args[3]=="q":
                quiet=True
            entry = args[0]
            change = args[1]
            mode = args[2]
            if mode=="add":
                self.__consumption[entry]=change+self.__consumption[entry]
            elif mode=="multiply":
                self.__consumption[entry]=change*self.__consumption[entry]
            else:
                print("ERROR: Mode unknown. Please choose add or multiply.")
            if not quiet:
                self.compute_consumption()
            self.__save_temp_consumption()
    
    def compute_consumption(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['compute_consumption'])
        else:
            if len(args)==1 and args[0]=="l":
                self.__quiet=False
            if len(args)>0 and type(args[0])==dict:
                self.__consumption=args[0]
                if len(args)==2 and args[1]=="l":
                    self.compute_consumption("l")
                else:
                    self.compute_consumption()
            sum=0
            for key in self.__consumption:
                sum = sum+self.__consumption[key]*self.__d_cal[key]
            if not self.__quiet:
                print("Calory consumption: " + self.__get_color(sum)+"{0:.2f}".format(sum) + " kcal" + "\033[0;0m")
                self.print_cal_demand()
            self.__sum=sum
        
    def save_consumption(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['save_consumption'])
        else:
            if len(args)==0:
                date=self.__get_date()
            else:
                date=args[0]
            if date[4:]=="0101":
                with open('data/'+date[:4]+'_cal_consumption.txt', 'w') as f1:
                    f1.write('#date\t\ttime\t\t\tkcal\n')
            with open('data/'+date[:4]+'_cal_consumption.txt', 'a') as f2:
                f2.write(date + "\t" + str(self.__date2time(date)) + "\t" + str(self.__sum) + "\n")
            self.__save_measures(date)
        
    def print_cal_demand(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['print_cal_demand'])    
        else:
            lot, upt = self.__create_demand()
            print("Current calory range: [" + str(lot) + ", " + str(upt) + "] kcal")
        
    def plot_consumption(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['plot_consumption']) 
        else:
            show=1
            if len(args)!=0 and args[0]==0:
                show=0
            year=self.__get_date()[:4]
            lot, upt = self.__create_demand()
            date, time, kcal = np.loadtxt("data/"+year+"_cal_consumption.txt", unpack=True)
            time_lin = np.linspace(int(year), int(year)+1, 800)
            upper_threshold = lot*np.ones(800)
            lower_threshold = upt*np.ones(800)
            mp.plot(time, kcal, ".")
            mp.plot(time_lin, upper_threshold)
            mp.plot(time_lin, lower_threshold)
            mp.xlabel("time [years]")
            mp.ylabel("calories [kcal]")
            mp.savefig("plots/"+year+"_cal_consumption.png")
            if show:
                mp.show()
    
    def plot_BMI(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['plot_BMI']) 
        else:
            show=1
            if len(args)!=0 and args[0]==0:
                show=0
            year=self.__get_date()[:4]
            date, time, weight, abdomen, neck = np.loadtxt("data/measures.txt", unpack=True)
            height = float(self.__d_user["height"])/100
            BMI=weight/pow(height,2)
            time_lin = np.linspace(int(year), int(year)+1, 800)
            underweight=18.5*np.ones(800)
            normal_weight=25*np.ones(800)
            overweight=30*np.ones(800)
            adipositas=35*np.ones(800)
            mp.plot(time, BMI, ".")
            mp.plot(time_lin, underweight, label="underweight")
            mp.plot(time_lin, normal_weight, label="normal weight")
            mp.plot(time_lin, overweight, label="overweight")
            mp.plot(time_lin, adipositas, label="adipositas")
            mp.xlabel("time [years]")
            mp.ylabel("BMI")
            mp.legend()
            mp.savefig("plots/"+year+"_BMI.png")
            if show:
                mp.show()
        
    def plot_body_fat(self, *args):
        if len(args)==1 and args[0]=="help":
            print(self.__d_help['plot_body_fat']) 
        else:
            show=1
            if len(args)!=0 and args[0]==0:
                show=0
            year=self.__get_date()[:4]
            date, time, weight, abdomen, neck = np.loadtxt("data/measures.txt", unpack=True)
            height = float(self.__d_user["height"])
            body_fat=86.010*np.log10(abdomen-neck)-70.041*np.log10(height)+30.29521038
            time_lin = np.linspace(int(year), int(year)+1, 800)
            underweight=8*np.ones(800)
            normal_weight=20*np.ones(800)
            overweight=25*np.ones(800)
            mp.plot(time, body_fat, ".")
            mp.plot(time_lin, underweight, label="underweight")
            mp.plot(time_lin, normal_weight, label="normal weight")
            mp.plot(time_lin, overweight, label="overweight")
            mp.xlabel("time [years]")
            mp.ylabel("Body fat percentage [%]")
            mp.legend()
            mp.savefig("plots/"+year+"_body_fat.png")
            if show:
                mp.show()
