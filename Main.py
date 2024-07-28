from StoreMenu import StoreMenu as SM

if __name__ == "__main__":
    store_menu = SM()
    store_menu.display()
    name = store_menu.name
    print(f"Thank You For Visiting {name} Store")