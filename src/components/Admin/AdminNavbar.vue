<template>
    <nav class="navbar navbar-expand-lg bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand text-light" href="">Admin Navbar</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
  
  
            <li class="nav-item">
              <router-link  class="nav-link active text-light" aria-current="page" to="/">Admin Home</router-link>
            </li>
  
            <li>
            <router-link class="nav-link active text-light" aria-current="page" to="/ManageCategory">Category Manage</router-link>
            </li>
            

            <li>
              <router-link class="nav-link active text-light" aria-current="page" to="/AdminManageBooks">Books Manage</router-link>
              </li>
            
  
  
   
  
  
  
          </ul>
          <form class="d-flex" role="search">
            <input
              class="form-control me-2 bg-dark text-light border border-success"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>
  </template>
  