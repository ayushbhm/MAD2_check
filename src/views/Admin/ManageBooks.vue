<template>
  <div>
    <AdminNavbar />
    <div class="admin-manage-books">
      <h1>Admin Manage Books</h1>
      <BooksBox />
    </div>
  </div>
</template>

<script>
import AdminNavbar from "@/components/Admin/AdminNavbar.vue";
import BooksBox from "@/components/Admin/BooksBox.vue";

export default {
  components: {
    AdminNavbar,
    BooksBox
  }
};
</script>

<style scoped>
.admin-manage-books {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
