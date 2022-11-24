const WebSocket = require('ws');

var table = {};
var dataf = {
	'binance': {
		'ask': {},
		'bid': {}
	},
	'okx': {
		'ask': {},
		'bid': {}
	}
};

// =============== BINANCE ===============
const binance_sock = new WebSocket(
	'wss://stream.binance.com:9443/ws/btcusdt@depth20@100ms'
);

binance_sock.on('message', msg => {
	str = msg.toString();
	json = JSON.parse(str);
	binance_bid = json['bids'][0][0]
	binance_ask = json['asks'][0][0]
	table['binance'] = {
			'bid': binance_bid,
			'ask': binance_ask,
			'time': Date.now()
	};
	dataf['binance']['ask'][Date.now()] = binance_ask
	dataf['binance']['bid'][Date.now()] = binance_bid
	render();
});

// ============== OKX ====================
const okx_sock = new WebSocket(
 'wss://wsaws.okx.com:8443/ws/v5/public',
);
okx_sock.on('open', () => {
	let plstr = {
		"op": "subscribe",
		"args": [
			{
				"channel": "books",
				"instId": "BTC-USDT"
			}
		]
	};
	let pljson = JSON.stringify(plstr);
	okx_sock.send(pljson);
});
okx_sock.on('message', (msg) => {
	str = msg.toString();
	try {
		json = JSON.parse(str)['data'][0];
		okx_ask = json['asks'][0][0];
		okx_bid = json['bids'][0][0];
		table['okx'] = {
			'bid': okx_bid,
			'ask': okx_ask,
			'time': Date.now()
		};
		render();
	} catch (e) {
	}
});


// ============== RENDER =================
function render() {
	console.clear();
	//update_spread();
	console.log(dataf);
}

function update_spread() {
	try {
		table['binance']['hypo'] = table['binance']['bid'] - table['okx']['ask'];
		table['okx']['hypo'] = table['okx']['bid'] - table['binance']['ask'];
		spreads['binance']
		spreads['okx']
	} catch (e) {
	}
}

