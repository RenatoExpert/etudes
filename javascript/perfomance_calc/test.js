/*
 * I was testing if making average with a lot of values were fast enought to be useful in a ccxt project i had
 */

'use strict'

const	max_vol	= 1000,
	min_vol	= 0,
	max_price	= 323,
	min_price	= 320;

let orderbook = {};

const	sort	= (min, max) => Math.floor ((max * Math.random ()) + min);

const	sort_vol	= () => sort (min_vol, max_price);

let test = 0;
for (let i = min_price; i < max_price; i+= 0.001) {
	orderbook[i] = sort_vol();
	test++;
}
console.table (orderbook);
console.info ('Fake orderbook generated');
console.info ('With', test, 'values');

//	Begin simulation
console.info ('Calculating average...');
let	initial_time	= new Date();
let	total_products	= 0;
let	total_volumes	= 0;
Object.keys (orderbook).forEach ( line => {
	total_products	+= line * orderbook [line];
	total_volumes	+= orderbook [line];
});
let	average	= total_products/total_volumes;
let	final_time	= new Date();
let	total_time	= final_time - initial_time;

console.info ('total (prices*volumes):', total_products);
console.info ('total volume:', total_volumes);
console.info ('average:', average);
console.info ('All calculation made in', total_time, 'miliseconds');

