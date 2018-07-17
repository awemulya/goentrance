<template>
  <table>
    <tr>
      <th>Subjects</th>
    </tr>
    <CourseListElement
      v-for="course in courses"
      :key="course.id"
      :course="course"
    />
    <tr class="table-row__fallback" v-if="!courses || courses.length === 0">
      <td colspan="3">No Courses Available</td>
    </tr>
  </table>
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
