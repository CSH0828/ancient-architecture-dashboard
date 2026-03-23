# data_loader.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json


class ArchitectureData:
    def __init__(self):
        self.data = self.load_all_data()
        self.history_data = []  # 先初始化
        self.sensor_data = self.generate_sensor_data()  # 再调用

    def load_all_data(self):
        """加载完整的古建筑数据集（12条记录）"""
        buildings = []

        # 皇宫类 (3个)
        palaces = [
            {'id': 1, 'name': '故宫太和殿', 'type': '皇宫', 'year': 1420, 'dynasty': '明',
             'province': '北京', 'lat': 39.916, 'lng': 116.397,
             'diameter': 45, 'dougong': 6.0, 'health': 95, 'scale': 5,
             'description': '中国现存最大木构宫殿，明清两代举行大典的场所'},
            {'id': 2, 'name': '沈阳故宫', 'type': '皇宫', 'year': 1625, 'dynasty': '清',
             'province': '辽宁', 'lat': 41.796, 'lng': 123.449,
             'diameter': 50, 'dougong': 5.5, 'health': 94, 'scale': 4,
             'description': '清初皇宫，中国仅存的两大宫殿建筑群之一'},
            {'id': 3, 'name': '南京明故宫', 'type': '皇宫', 'year': 1366, 'dynasty': '明',
             'province': '江苏', 'lat': 32.058, 'lng': 118.796,
             'diameter': 48, 'dougong': 5.8, 'health': 88, 'scale': 4,
             'description': '明朝京师应天府的皇宫，中世纪世界规模最大宫殿建筑群'},
        ]

        # 民居类 (3个)
        residences = [
            {'id': 4, 'name': '平遥古城', 'type': '民居', 'year': 1370, 'dynasty': '明',
             'province': '山西', 'lat': 37.202, 'lng': 112.550,
             'diameter': 60, 'dougong': 2.5, 'health': 88, 'scale': 4,
             'description': '明清时期汉族城市的杰出范例，保存最完整的古城之一'},
            {'id': 5, 'name': '福建土楼', 'type': '民居', 'year': 1200, 'dynasty': '宋',
             'province': '福建', 'lat': 24.629, 'lng': 116.917,
             'diameter': 65, 'dougong': 2.0, 'health': 90, 'scale': 3,
             'description': '客家民居的典型代表，适应山区环境的防御性聚居建筑'},
            {'id': 6, 'name': '北京四合院', 'type': '民居', 'year': 1400, 'dynasty': '明',
             'province': '北京', 'lat': 39.940, 'lng': 116.407,
             'diameter': 55, 'dougong': 2.2, 'health': 85, 'scale': 2,
             'description': '华北地区传统合院式建筑，体现传统礼制与家族观念'},
        ]

        # 桥梁类 (3个)
        bridges = [
            {'id': 7, 'name': '赵州桥', 'type': '桥梁', 'year': 605, 'dynasty': '隋',
             'province': '河北', 'lat': 37.758, 'lng': 114.660,
             'diameter': 80, 'dougong': 1.2, 'health': 92, 'scale': 5,
             'description': '世界现存最早、保存最完整的敞肩石拱桥'},
            {'id': 8, 'name': '卢沟桥', 'type': '桥梁', 'year': 1189, 'dynasty': '金',
             'province': '北京', 'lat': 39.856, 'lng': 116.214,
             'diameter': 75, 'dougong': 1.5, 'health': 89, 'scale': 4,
             'description': '北京市现存最古老的石造联拱桥，见证七七事变'},
            {'id': 9, 'name': '洛阳桥', 'type': '桥梁', 'year': 1053, 'dynasty': '宋',
             'province': '福建', 'lat': 24.909, 'lng': 118.586,
             'diameter': 78, 'dougong': 1.3, 'health': 91, 'scale': 4,
             'description': '中国现存最早的跨海梁式大石桥，首创"筏型基础"'},
        ]

        # 官府类 (3个)
        offices = [
            {'id': 10, 'name': '内乡县衙', 'type': '官府', 'year': 1304, 'dynasty': '元',
             'province': '河南', 'lat': 33.052, 'lng': 111.850,
             'diameter': 70, 'dougong': 3.0, 'health': 85, 'scale': 3,
             'description': '中国唯一保存最完整的封建时代县级官署衙门'},
            {'id': 11, 'name': '平遥县衙', 'type': '官府', 'year': 1346, 'dynasty': '元',
             'province': '山西', 'lat': 37.206, 'lng': 112.553,
             'diameter': 68, 'dougong': 3.2, 'health': 87, 'scale': 3,
             'description': '中国现有保存完整的四大古衙之一'},
            {'id': 12, 'name': '霍州署', 'type': '官府', 'year': 1303, 'dynasty': '元',
             'province': '山西', 'lat': 36.569, 'lng': 111.725,
             'diameter': 72, 'dougong': 2.8, 'health': 86, 'scale': 3,
             'description': '中国古代州级衙署的典型代表'},
        ]

        buildings = palaces + residences + bridges + offices
        return pd.DataFrame(buildings)

    def generate_sensor_data(self):
        """生成实时传感器数据"""
        current_hour = datetime.now().hour
        minute = datetime.now().minute

        # 模拟昼夜温度变化
        base_temp = 18 + 8 * np.sin(current_hour / 24 * 2 * np.pi)
        # 模拟湿度变化
        base_humidity = 55 + 15 * np.sin(current_hour / 12 * 2 * np.pi)
        # 模拟游客人数（白天多，晚上少）
        if 8 <= current_hour <= 18:
            base_visitors = 500 + 300 * np.sin((current_hour - 8) / 10 * np.pi)
        else:
            base_visitors = 100

        # 添加随机波动
        temp = round(base_temp + random.uniform(-1.5, 1.5), 1)
        humidity = round(base_humidity + random.uniform(-3, 3), 1)
        visitors = int(base_visitors + random.uniform(-50, 50))

        # 随机生成1-3个预警
        alert_count = random.choices([0, 1, 2, 3], weights=[0.6, 0.2, 0.15, 0.05])[0]
        alerts = []
        if alert_count > 0:
            alert_types = ['裂缝扩大', '结构变形', '湿度超标', '温度异常', '游客超载']
            buildings = random.sample(self.data['name'].tolist(), min(alert_count, len(self.data)))
            for building in buildings:
                alerts.append({
                    'building': building,
                    'type': random.choice(alert_types),
                    'level': random.choice(['低', '中', '高']),
                    'time': datetime.now().strftime('%H:%M')
                })

        # 记录历史数据（最近20条）
        sensor_record = {
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'temperature': temp,
            'humidity': humidity,
            'visitors': visitors,
            'alerts': alerts
        }

        self.history_data.append(sensor_record)
        if len(self.history_data) > 20:
            self.history_data = self.history_data[-20:]

        return sensor_record

    def filter_data(self, dynasty=None, building_type=None, year_range=(500, 1911), province=None):
        """筛选数据"""
        df = self.data.copy()

        if dynasty and dynasty != '全部':
            df = df[df['dynasty'] == dynasty]

        if building_type and building_type != '全部':
            if isinstance(building_type, list):
                df = df[df['type'].isin(building_type)]
            else:
                df = df[df['type'] == building_type]

        if province and province != '全部':
            df = df[df['province'] == province]

        df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
        return df

    def get_summary(self, df=None):
        """获取统计摘要"""
        if df is None:
            df = self.data

        if len(df) == 0:
            return {
                'count': 0,
                'avg_diameter': 0,
                'avg_dougong': 0,
                'avg_health': 0,
                'warning_count': 0
            }

        # 计算预警数量（健康度<90）
        warning_count = len(df[df['health'] < 90])

        return {
            'count': len(df),
            'avg_diameter': round(df['diameter'].mean(), 1),
            'avg_dougong': round(df['dougong'].mean(), 2),
            'avg_health': round(df['health'].mean(), 1),
            'warning_count': warning_count
        }

    def get_dynasty_stats(self):
        """获取朝代统计"""
        dynasties = []
        for dynasty in self.data['dynasty'].unique():
            df = self.data[self.data['dynasty'] == dynasty]
            dynasties.append({
                'name': dynasty,
                'count': len(df),
                'avg_diameter': round(df['diameter'].mean(), 1),
                'avg_health': round(df['health'].mean(), 1)
            })
        return sorted(dynasties, key=lambda x: x['count'], reverse=True)

    def get_type_stats(self):
        """获取类型统计"""
        types = []
        for building_type in self.data['type'].unique():
            df = self.data[self.data['type'] == building_type]
            types.append({
                'name': building_type,
                'count': len(df),
                'avg_diameter': round(df['diameter'].mean(), 1),
                'avg_dougong': round(df['dougong'].mean(), 2)
            })
        return types

    def get_building_detail(self, building_id):
        """获取建筑详情"""
        building = self.data[self.data['id'] == building_id]
        if len(building) == 0:
            return None
        return building.iloc[0].to_dict()
