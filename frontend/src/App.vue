<template>
  <div id="app">
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="title" v-model="book.title">
        <input type="text" class="form-control col-3 mx-2" placeholder="author" v-model="book.author">
        <input type="text" class="form-control col-3 mx-2" placeholder="year" v-model="book.year">
        <button class="btn btn-success">Submit</button>
      </div>
    </form>
    <table class="table">
        <thead>
            <th>Title</th>
            <th>Author</th>
            <th>Year</th>
            <th></th>
        </thead>
        <tbody>
            <tr v-for="book in books" :key="book.id" @dblclick="$data.book = book">
                <td>{{ book.title }}</td>
                <td>{{ book.author }}</td>
                <td>{{ book.year }}</td>
                <td>
                    <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteBook(book)">X</button>
                </td>
            </tr>
        </tbody>
    </table>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
        return {
            book: {
              'title': '',
              'author': '',
              'year': '',

            },
            books: []
        }
    },
  async created(){
        await this.getBooks();
  },

  methods: {
        submitForm(){
          if (this.book.id === undefined){
            this.createBook();
          } else {
            this.editBook();
          }

        },
        async getBooks(){
          var response = await fetch('http://127.0.0.1:8000/api/books/');
          this.books = await response.json();

        },
        async createBook(){
          await this.getBooks();

          await fetch('http://127.0.0.1:8000/api/books/', {
            method: 'post',
            headers: {
              'content-Type': 'application/json'
            },
            body: JSON.stringify(this.book)
          });
            await this.getBooks();
            this.book = {};

        },
        async editBook(){
          await this.getBooks();

          await fetch(`http://127.0.0.1:8000/api/books/${this.book.id}/`, {
            method: 'put',
            headers: {
              'content-Type': 'application/json'
            },
            body: JSON.stringify(this.book)
          });
            await this.getBooks();
            this.book = {};

        },
        async deleteBook(book){
          await this.getBooks();

          await fetch(`http://127.0.0.1:8000/api/books/${book.id}/`, {
            method: 'delete',
            headers: {
              'content-Type': 'application/json'
            },
            body: JSON.stringify(this.book)
          });
            await this.getBooks();

        }
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
