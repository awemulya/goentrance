<template>
  <v-layout
          justify-center
          align-center=""
        >
        <v-flex xs 12>
    <CourseListElement
      v-for="course in courses"
      :key="course.id"
      :course="course"
    />
        </v-flex>
    <table>
    <tr class="table-row__fallback" v-if="!courses || courses.length === 0">
      <td colspan="3">No Courses Available</td>
    </tr>
  </table>
  </v-layout>
</template>

<script>
import CourseListElement from './CourseListElement'

export default {
  name: 'CourseList',
  components: {
    CourseListElement
  },
  props: {
    courses: {
      type: Array
    }
  }
}
</script>

<style scoped>

</style>
