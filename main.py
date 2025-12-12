# Basit bir birim dönüştürücü programı
# Rüveyda tarafından yazıldı :)

def km_to_miles(km):
    """Kilometreyi mile çevirir."""
    return km * 0.621371

def c_to_f(c):
    """Celsius'u Fahrenheit'a çevirir."""
    return (c * 9/5) + 32

def display_menu():
    print("\n--- Birim Dönüştürücü ---")
    print("1) Kilometre → Mil")
    print("2) Celsius → Fahrenheit")
    print("3) Çıkış")

def main():
    print("Hoş geldiniz! Küçük birim dönüştürücü programı başlatılıyor...")
    while True:
        display_menu()
        choice = input("Seçiminiz (1-3): ").strip()

        if choice == "1":
            try:
                km = float(input("Kilometre değerini girin: "))
                print(f"{km} km = {km_to_miles(km):.2f} mil")
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")

        elif choice == "2":
            try:
                c = float(input("Celsius değerini girin: "))
                print(f"{c}°C = {c_to_f(c):.2f}°F")
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")

        elif choice == "3":
            print("Programdan çıkılıyor... Görüşmek üzere 👋")
            break

        else:
            print("Geçersiz seçim, lütfen 1-3 arasında bir değer girin.")

if __name__ == "__main__":
    main()

