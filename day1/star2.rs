use std::str::FromStr;
const INPUT: &str = include_str!("./input.txt");

fn main(){
    let mut left = Vec::new();
    let mut right = Vec::new();
    for line in INPUT.lines(){
        let splitted: Vec<isize> = line.split_whitespace().map(|x| isize::from_str(x).unwrap()).collect();
        left.push(splitted[0]);
        right.push(splitted[1]);
    }
    left.sort();
    right.sort();

    let sum: isize = (0..left.len()).map(|i| (left[i] - right[i]).abs()).sum();
    println!("{}", sum);

    let similarity: isize = left.iter().map(|l| right.iter().filter(|r| *r == l).count() as isize * l).sum();
    println!("{}", similarity);
}