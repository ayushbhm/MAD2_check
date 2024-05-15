import axios from 'axios'

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:5000',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  get_book_details() {
    return apiClient.get('/api/admin_get_book_details')
  },

  updateBookDetails(bookId, updatedBookData) {
    const url = `/api/admin_update_book/${bookId}`;
    return apiClient.post(url, updatedBookData)
      .then(response => {
        return response.data; // Return response data upon successful update
      })
      .catch(error => {
        throw error; // Propagate error to caller for handling
      });
  },
  getBookCategories() {
    return apiClient.get('/api/admin_get_categories')
  }
,


admin_delete_book(bookId){

  const url = '/admin_delete_book/${book_id}';
  return apiClient.delete(url,bookId)
  .then(response => {
    return response.data; // Return response data upon successful update
  })
  .catch(error => {
    throw error; // Propagate error to caller for handling
  });
  



}

}