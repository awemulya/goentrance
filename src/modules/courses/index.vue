<template>
  <CourseList :courses="courses" />
</template>

<script>
import { mapGetters } from 'vuex'
import store from './_store'
import CourseList from './_components/CourseList'

export default {
  name: 'CourseModule',
  components: {
    CourseList
  },
  computed: {
    ...mapGetters({
      courses: '$_courses/courses'
    })
  },
  created () {
    const STORE_KEY = '$_courses'
    // eslint-disable-next-line no-underscore-dangle
    if (!(STORE_KEY in this.$store._modules.root._children)) {
      this.$store.registerModule(STORE_KEY, store)
    }
  },
  mounted () {
    this.$store.dispatch('$_courses/getCourses')
  }
}
</script>
