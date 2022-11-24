const WebSocket = require('ws');
const fs = require('fs');

startTime = new Date();

function killme () {
	secs = process.argv[2] || 30;
	limit = secs*1000;
	past = new Date().getTime() - startTime.getTime();
	ready = past >= limit;
	if (ready) {
		var dataf = {
			'binance': binancef,
			'okx': okxf
		};
		console.log('Time to export');
		exportable = JSON.stringify(dataf);
		fs.writeFileSync('./dataframe.json', exportable);
		console.log('Done!');
		process.exit(0);
	} else {
		console.clear();
		console.log('Past ' + Math.round(past/1000) + ' from ' + limit/1000);
		console.log('\t', Math.round((100*past)/limit) + '%');
	}
}

var table = {};

var binancef= {};

var okxf= {};

// =============== BINANCE ===============
const binance_sock = new WebSocket(
	'wss://stream.binance.com:9443/ws/btcusdt@depth20@100ms'
);

binance_sock.on('message', msg => {
	str = msg.toString();
	json = JSON.parse(str);
	binance_bid = json['bids'][0][0]
	binance_ask = json['asks'][0][0]
	dtime = new Date().getTime() - startTime;
	binancef[dtime] = {
		'ask': binance_ask,
		'bid': binance_bid
	};
	killme();
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
		dtime = new Date().getTime() - startTime;
		okxf[dtime] = { 
			'ask': okx_ask,
			'bid': okx_bid
		};
		killme();
	} catch (e) {
	}
});


