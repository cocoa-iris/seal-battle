import random

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        reduced_damage = max(damage - self.defense, 0)
        self.hp = max(self.hp - reduced_damage, 0)
        return reduced_damage

    def attack_target(self, target):
        damage = random.randint(self.attack - 5, self.attack + 5)
        actual_damage = target.take_damage(damage)
        return actual_damage


class Game:
    def __init__(self):
        self.player = Character("Player", 100, 20, 5)
        self.enemy = Character("Enemy", 80, 15, 3)

    def player_turn(self):
        print("\n[プレイヤーのターン]")
        print("1. 攻撃")
        print("2. 防御")
        choice = input("選択してください (1/2): ")
        if choice == "1":
            damage = self.player.attack_target(self.enemy)
            print(f"プレイヤーが敵に {damage} ダメージを与えた！")
        elif choice == "2":
            print("プレイヤーは防御の体勢を取った！")
        else:
            print("無効な選択肢です。")

    def enemy_turn(self):
        print("\n[敵のターン]")
        damage = self.enemy.attack_target(self.player)
        print(f"敵がプレイヤーに {damage} ダメージを与えた！")

    def play(self):
        print("ターン制バトルゲームへようこそ！")
        while self.player.is_alive() and self.enemy.is_alive():
            self.player_turn()
            if self.enemy.is_alive():
                self.enemy_turn()
            print(f"\nプレイヤーのHP: {self.player.hp}")
            print(f"敵のHP: {self.enemy.hp}")

        if self.player.is_alive():
            print("\nプレイヤーの勝利！")
        else:
            print("\n敵の勝利！")


# ゲームを実行
if __name__ == "__main__":
    game = Game()
    game.play()
