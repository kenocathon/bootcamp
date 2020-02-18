class Book {
  constructor(author, title, price) {
    this.author = author;
    this.title = title;
    this.price = price;
  }
  toString() {
    return `${this.author}: ${this.title} (\$${this.price})`;
  }
}

const oldBook = new Book("Miguel de Cervantes", "Don Quixote", "29.99");
const actionBook = new Book("Tom Clancy", "Red Rabbit", "54.22");

function showString(book1, book2) {
  document.getElementById("display-book1").innerHTML = book1;
  document.getElementById("display-book2").innerHTML = book2;
}

showString(oldBook, actionBook);
