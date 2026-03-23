# app.py
from flask import Flask, render_template, jsonify, request
from datetime import datetime
from data_loader import ArchitectureData
import json

app = Flask(__name__)
data_manager = ArchitectureData()


@app.route('/')
def index():
    return render_template('dashboard.html',
                           title="中国古代建筑智慧监测平台",
                           current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


@app.route('/api/architecture-data')
def get_architecture_data():
    """获取古建筑数据（支持筛选）"""
    dynasty = request.args.get('dynasty', '全部')
    building_type = request.args.get('type', '全部')
    province = request.args.get('province', '全部')

    if building_type != '全部':
        building_type = building_type.split(',')

    df = data_manager.filter_data(
        dynasty=dynasty,
        building_type=building_type,
        province=province
    )

    return jsonify({
        'table_data': df.to_dict('records'),
        'summary': data_manager.get_summary(df),
        'sensor_data': data_manager.sensor_data,
        'dynasty_list': list(data_manager.data['dynasty'].unique()),
        'type_list': list(data_manager.data['type'].unique()),
        'province_list': list(data_manager.data['province'].unique())
    })


@app.route('/api/real-time')
def get_real_time_data():
    """获取实时传感器数据"""
    data_manager.sensor_data = data_manager.generate_sensor_data()
    return jsonify({
        'sensor': data_manager.sensor_data,
        'history': data_manager.history_data[-10:]  # 最近10条历史
    })


@app.route('/api/dynasty-trend')
def get_dynasty_trend():
    """获取朝代趋势数据"""
    return jsonify(data_manager.get_dynasty_stats())


@app.route('/api/type-stats')
def get_type_stats():
    """获取类型统计数据"""
    return jsonify(data_manager.get_type_stats())


@app.route('/api/building-detail/<int:building_id>')
def get_building_detail(building_id):
    """获取建筑详情"""
    detail = data_manager.get_building_detail(building_id)
    if detail:
        return jsonify(detail)
    return jsonify({'error': '建筑不存在'}), 404


@app.route('/api/all-data')
def get_all_data():
    """获取所有数据（用于地图）"""
    return jsonify(data_manager.data.to_dict('records'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
