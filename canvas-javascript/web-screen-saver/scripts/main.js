const canvas = document.querySelector("canvas");
cx = 800;
cy = 600;
canvas.width = cx;
canvas.height = cy;
ctx = canvas.getContext('2d');
ctx.strokeStyle = 'red';
color_option = ['red','blue','yellow','pink','green','brown','black','cyan']
sizex = 100;
sizey = 100;

var x, y, v_x, v_y, maxturn, turn;

function clearscreen() {
	if (getRandomInt(2)-1) {
		 ctx.clearRect(0, 0, cx, cy);
	}
}

function reset() {
	x = getRandomInt(700);
	y = getRandomInt(500);
	v_x = getRandomInt(6)+1;
	v_y = getRandomInt(6)+1;
	maxturn = getRandomInt(20);
	turn = 0;
	clearscreen();
	console.log(maxturn);
}

function getRandomInt(max) {
	return Math.floor(Math.random() *max);
}

function changeColor() {
	ctx.strokeStyle = color_option[getRandomInt(color_option.length)-1];
}

function collided() {
	changeColor();
	turn++;
	console.log(turn+'/'+maxturn);
}

function next () {
	x += v_x;
	y += v_y;
	if ( 0 >= x || x > cx-sizex) {
		v_x = -v_x;
		collided();
	}
	if ( 0 >= y || y > cy-sizey) {
		v_y = -v_y;
		collided();
	}
	if (turn >= maxturn) {
		reset();
	}
}

function draw () {
	ctx.strokeRect (x,y,sizex,sizey);
	next();
	requestAnimationFrame(draw);
}
reset();
draw();
