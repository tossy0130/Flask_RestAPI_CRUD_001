from flask import Flask, jsonify, request
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策

# 大本データ　※ここに、データを追加したり、削除したりしていく。
items = [{'id' : 1, 'name': 'tossy_01', 'price': 1024}, {'id':2, 'name': '夏目智徹', 'price': 8888888888}]

# （表示）GETメソッドで全てのアイテムを返すエンドポイント
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})

#（登録） POSTメソッドで新しいアイテムを作成するエンドポイント　
@app.route('/items', methods=['POST'])
def create_item():
   # JSONを受け取る
    json = request.get_json()
    
    # JSONをパースする
    name = json['name']
    price = json['price']
    item = {'name': name, 'price': price}
    item_id = len(items) + 1
    items.append(item)
    
     # 返却用ディクショナリを構築
    item['id'] = item_id
    return jsonify(item)  # JSONをレスポンス


# （検索）GETメソッドで特定のアイテムを返すエンドポイント
@app.route('/items/<string:item_name>', methods=['GET'])
def get_item(item_name):
    for item in items:
        if item['name'] == item_name:
            return jsonify(item)
    return jsonify({'message': 'エラー 404.'}), 404

#（更新） PUTメソッドで特定のアイテムを更新するエンドポイント
@app.route('/items/<string:item_name>', methods=['PUT'])
def update_item(item_name):
    for item in items:
        if item['name'] == item_name:
            item['price'] = request.json['price']
            return jsonify(item)
    return jsonify({'message': 'エラー 404.'}), 404

#（削除）DELETEメソッドで特定のアイテムを削除するエンドポイント
@app.route('/items/<string:item_name>', methods=['DELETE'])
def delete_item(item_name):
    for item in items:
        if item['name'] == item_name:
            items.remove(item)
            return jsonify({'message': 'deleted OK'})
    return jsonify({'message': 'エラー 404.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
