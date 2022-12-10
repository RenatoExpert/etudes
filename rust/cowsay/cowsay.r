use std::env;

fn main() {
	let text = format!("{}", env::args().nth(1).expect("no pattern given"));
	println!(" ______ ");
	println!("< {} >", text);
	println!(" ------ ");
	println!("        \\   ^__^");
	println!("         \\  (oo)\\_______");
	println!("            (__)\\       )\\/\\");
	println!("                ||----w |");
	println!("                ||     ||");
}
