<template>
  <div>
    <!-- <h1>Welcome</h1> -->
    <CoursesContainer />
  </div>
</template>

<script>
import CoursesContainer from '@/modules/subjects'

export default {
  name: 'Subject',
  components: {
    CoursesContainer
  }
}
</script>

<style scoped>
h1 {
  font-family: "Raleway", "Helvetica Neue", Helvetica, Arial, sans-serif;
  text-align: center;
  font-weight: 100;
  font-size: 3em;
  letter-spacing: 0.05em;
  color: #4b4b4b;
}
</style>
