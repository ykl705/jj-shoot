from save_loader import load_game

class Settings():
    def __init__(self):

        list=load_game('data.pkl')


        self.screen_width=700
        self.screen_height=480
        self.bg_color=(255,255,255)

        self.jj_speed_factor=5
        self.jj_limit=15+list[1]

        self.bullet_speed_factor=5
        self.bullet_width=5
        self.bullet_height=5
        self.bullet_color=200,200,0
        self.bullet_chuan=1
        self.bullet_damage=15.0+list[4]
        self.bullet_energy_cost=0.0
        self.bullet_penetrate=False

        self.skill_width=20
        self.skill_height=400
        self.skill_damage=25.0
        self.skill_energy_cost = 50.0

        self.skill_penetrate=True
        self.bi_speed_factor=1.0-list[3]
        self.bi_number=10+list[0]
        self.bi_health=15
        self.bi_damage=1
        self.fleet_drop_speed=[1,2,1.5,0,0]
        self.fleet_drop_speed1=[1,2,1.5]
        self.fleet_direction=1

        self.boss1_health = 100000.0
        self.boss2_health = 7500.0
        self.boss_virus_health =150000.0
        self.boss_magic_health =250000.0

        self.speedup_cale=1.0001
        self.jj_speedup_cale=1.0001
        self.score_scle=1.0001
        self.bi_health_scle=1.001
        self.damage_scle=1.001

        self.music_volume =0.5



        # self.final_heart_health = 99999999999999.0
        self.final_heart_health = 999999.0
        self.final_heart_health_regenerate = 100
        self.final_heart_drop_speed = 0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        list = load_game('data.pkl')

        self.jj_speed_factor=3
        self.bullet_speed_factor=5
        self.bi_speed_factor=1-list[3]
        self.bi_points=12+list[2]


    def increase_speed(self):
        self.jj_speed_factor*=self.jj_speedup_cale
        self.jj_speed_list=[self.jj_speed_factor,4.000]
        self.jj_speed_factor=float(min(self.jj_speed_list))
        self.bullet_speed_factor*=self.speedup_cale
        self.bi_speed_factor*=self.speedup_cale
        self.bi_points=float(self.bi_points*self.score_scle)
        self.bullet_width =float(1.0001*self.bullet_width)
        self.bi_number =float(1.0001*self.bi_number)
        self.bi_health =float(self.bi_health*self.bi_health_scle)
        self.bullet_damage=float(self.bullet_damage*self.damage_scle)