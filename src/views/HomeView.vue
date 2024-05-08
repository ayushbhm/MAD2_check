<script setup>

import Studentnavbar from '../components/Studentcomponents/Studentnavbar.vue'

import BookBox from '../components/Studentcomponents/AllBooksBox.vue'
import BooksStatusBox  from'../components/Studentcomponents/PendingBooksBox.vue'
import ApprovedBooksVue from '../components/Studentcomponents/ApprovedBooks.vue'


import LoginForm from '@/components/LoginForm.vue'
import BooksStatusBoxVue from '@/components/Studentcomponents/PendingBooksBox.vue'



</script>

<template>
  <main>

    
   <Studentnavbar/>
   All Books
   <BookBox/>

 

   My Approved books
   <ApprovedBooksVue/>

  </main>
 
</template>
