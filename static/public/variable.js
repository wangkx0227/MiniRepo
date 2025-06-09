// 变量
export const API_BASE_URL = 'https://api.example.com';

// 导出函数
export function add(a, b) {
  return a + b;
}

// 导出类
export class Person {
  constructor(name) {
    this.name = name;
  }
  sayHi() {
    console.log(`Hi, I'm ${this.name}`);
  }
}