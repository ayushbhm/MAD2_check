<template>
  Approved Books
  <div style="display: flex; flex-wrap: wrap; justify-content: space-around">
    <div
      v-for="(book, index) in approvedBooks"
      :key="index"
      style="
        width: 30%;
        height: 300px;
        margin-bottom: 20px;
        background-color: rgba(255, 255, 255, 0.15);
        border: 1px solid #000;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
      "
    >
      <h2 style="font-size: 24px">{{ book.title }}</h2>
      <p
        style="
          font-size: 16px;
          text-align: left;
          margin-top: 20px;
          color: aliceblue;
          margin-bottom: 20px;
        "
      >
        Author: {{ book.author }}
      </p>
      <p style="font-size: 14px; text-align: left; color: aliceblue; margin-bottom: 20px">
        Category: {{ book.category }}
      </p>

      <p style="font-size: 12px; text-align: left; color: aliceblue; margin-bottom: 20px">
        Issue Date: {{ book.issue_date }}
      </p>

      <p style="font-size: 12px; text-align: left; color: aliceblue; margin-bottom: 20px">
        Due  Date: {{ book.return_date }}
      </p>
      <button
        style="
          background-color: green;
          color: white;
          border: none;
          padding: 10px 20px;
          border-radius: 5px;
        "
        @click="navigateToViewBook(book.book_id)"
      >
        Read Book
      </button>

      <a href="#" style="color: aliceblue; font-size: small; font-style: italic; margin-top: 20px;">Read Reviews</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:5000'

export default {
  data() {
    return {
      approvedBooks: []
    }
  },
  mounted() {
    this.getApprovedBooks()
  },
  methods: {
    getApprovedBooks() {
      axios
        .get('/api/get_approved_books') // Fetch only approved books
        .then((response) => {
          this.approvedBooks = response.data // Assign approved books to the approvedBooks array
        })
        .catch((error) => {
          console.error('Error fetching approved books:', error)
        })
    },
    readBook(bookId) {
      this.$router.push({ name: 'view-book', params: { bookId: bookId }});
    },

    navigateToViewBook(bookId) {
    // Push the route with the bookId parameter to the named route 'view-book'
    this.$router.push({ name: 'view-book', params: { bookId: bookId }});
  }
  
  }
}
</script>
