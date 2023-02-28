#[allow(dead_code)]
pub fn print_string_array(arr: &[String]) {
    for value in arr.iter() {
        print!("{} ", value)
    }
}

pub fn print_int_array(arr: &[i32]) {
    for value in arr.iter() {
        print!("{} ", value)
    }
}

#[allow(dead_code)]
pub fn print_vector(vec: Vec<i32>) {
    for value in &vec {
        print!("{} ", value)
    }
}

#[allow(dead_code)]
pub fn swap(param_int_array: &mut [i32], i: usize, j: usize) {
    let temp = param_int_array[i];
    param_int_array[i] = param_int_array[j];
    param_int_array[j] = temp;
}

#[allow(dead_code)]
pub fn get_max(arr: &[i32]) -> i32 {
    let mut max = arr[0];
    for i in 0..arr.len() {
        if arr[i] > max {
            max = arr[i];
        }
    }
    max
}

#[allow(dead_code)]
pub fn get_min(arr: &[i32]) -> i32 {
    let mut min = arr[0];
    for i in 0..arr.len() {
        if arr[i] < min {
            min = arr[i];
        }
    }
    min
}
