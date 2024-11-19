from math import *

delta_v = 11186
Isp = 350
m0 = 12550
mf = 2500
g0 = 9.81  # Earth gravitational acceleration in m/s²
Th = 2278000 # Space Shuttle Main Engine (SSME)

print("Rocket to Orbit")

def calc_delta_v(Isp, g0, m0, mf):
    # Tsiolkovsky rocket equation
    return Isp * g0 * log(m0 / mf)

def print_params(delta_v, Isp, m0, mf):
    print("")
    delta_v = calc_delta_v(Isp, g0, m0, mf)
    print("Delta-v: {:,.0f} m/s".format(delta_v))
    print("Thrust: {:,.0f} kN".format(Th / 1000))
    print("Isp: {} s".format(Isp))
    print("Initial mass (m0): {:,} kg".format(m0))
    print("Final mass (mf): {:,.0f} kg".format(mf))
    years, month, days, hours, minutes, seconds = calculate_burn_time(m0, mf, Isp, Th)
    burn_time_str = []
    if years > 0:
        burn_time_str.append("{:,} y".format(years))
    if month > 0:
        burn_time_str.append("{:,} M".format(month))
    if days > 0:
        burn_time_str.append("{:,} d".format(days))
    if hours > 0:
        burn_time_str.append("{} h".format(hours))
    if minutes > 0:
        burn_time_str.append("{} m".format(minutes))
    if seconds > 0:
        burn_time_str.append("{:.0f} s".format(seconds))
    burn_time_output = ", ".join(burn_time_str)

    print("Burn time:", burn_time_output)


def calculate_burn_time(m0, mf, Isp, F):
    g0 = 9.81  # 重力加速度 (m/s^2)
    ve = Isp * g0
    mdot = F / ve
    time = (m0 - mf) / mdot
    # 時間を日, 時, 分, 秒に変換
    years = int(time // 31558149.76)
    time = time % 31558149.76
    month = int(time // (30 * 24 * 3600))
    time = time % (30 * 24 * 3600)
    days = int(time // (24 * 3600))
    time = time % (24 * 3600)
    hours = int(time // 3600)
    time %= 3600
    minutes = int(time // 60)
    seconds = time % 60
    
    return years, month, days, hours, minutes, seconds


print("\nRocket Equation Solver")
print_params(delta_v, Isp, m0, mf)

while True:
    print(" [0] Quit [1] Calculate dv\n[7] Thrust [8] Isp [9] Delta")

    choice = input("Enter choice > ")
    
    if choice == "0":
        print("Quit")
        break
    elif choice == "1":
        Th_Input = input("Enter Thrust ({:,}) N> ".format(Th))
        if Th_Input.strip():
            Th = float(Th_Input)
        else:
            Th = Th
        Isp_Input = input("Enter Isp ({:,})> ".format(Isp))
        if Isp_Input.strip():
            Isp = float(Isp_Input)
        else:
            Isp = Isp
        m0_Input = input("Enter initial mass in kg ({:,})> ".format(m0))
        if m0_Input.strip():
            m0 = float(m0_Input)
        else:
            m0 = m0
        mf_Input = input("Enter payload mass in kg ({:,})> ".format(mf))
        if mf_Input.strip():
            mf = float(mf_Input)
        else:
            mf = mf

        if m0 > mf > 0:
            delta_v = calc_delta_v(Isp, g0, m0, mf)
            print_params(delta_v, Isp, m0, mf)
        else:
            print("Error: Mass values should be positive and initial mass m0 should be greater than final mass mf.")
        print_params(delta_v, Isp, m0, mf)

    elif choice == "7":
        print("Hayabusa2 40mN\nMule 6kN\nNuclear Rocket 35kN\nH2A 1st 2,520kN\nSaturnV 1st 7,740Kn\n")
        Th_Input = input("Enter Isp ({:,}) N> ".format(Th))
        if Th_Input.strip():
            Th = float(Th_Input)
        else:
            Th = Th
        print("Thrust {:,}".format(Th))
        print_params(delta_v, Isp, m0, mf)

    elif choice == "8":
        print("ION 3000s\nLOX/LH2: 453s\nKerosene/LOX 300s\nSolid 250-300 s\nElectric: 2,000 s")
        Isp_Input = input("Enter Isp ({:,}) s> ".format(Isp))
        if Isp_Input.strip():
            Isp = float(Isp_Input)
        else:
            Isp = Isp
        print_params(delta_v, Isp, m0, mf)

    elif choice == "9":
        print("1st Orbital dv: 7,900 m/s\n2nd Esc.Tera dv: 11,200 m/s\n3rd Esc.Sol dv: 16,700 m/s\n4th Esc.Galaxy: 41,200 m/s")

