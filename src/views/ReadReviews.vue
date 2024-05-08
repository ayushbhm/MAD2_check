<template>
  <div >
    
    <StudentNavbar />
   
    <p style="padding: 10px; color: green; font-weight: bold; font-size: 20px;">Book Reviews</p>
    <div v-if="reviews.length === 0">No reviews available for this book.</div>
    <div v-else>
      <!-- Display book information -->
      <div class="book-info">
        <h2>Book: {{ reviews[0].title }}</h2>
        <p>Author: {{ reviews[0].author }}</p>
        <p>Category: {{ reviews[0].category }}</p>
      </div>

      <!-- Display reviews list -->
      <ul class="reviews-list">
        <li v-for="(review, index) in reviews" :key="index" class="review">
          <p>{{ review.review }}  - {{ review.username }}</p>
          
         
        </li>
      </ul>
    </div>
  </div>
</template>

  
  <script setup>
  import axios from 'axios';
  import StudentNavbar from '../components/Studentcomponents/Studentnavbar.vue';
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  
  // Set base URL for Axios
  axios.defaults.baseURL = 'http://127.0.0.1:5000';
  
  // Define initial reviews as an empty array
  const reviews = ref([]);
  
  // Get current route
  const route = useRoute();
  
  // Fetch reviews data from Flask API
  onMounted(async () => {
    try {
      const response = await axios.get(`/readreviews/${route.params.bookId}`);
      reviews.value = response.data;
    } catch (error) {
      console.error('Error fetching reviews:', error);
    }
  });
  </script>
  
  <style scoped>
  /* Add your CSS styling here */
  </style>
  