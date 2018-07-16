<template>
  <table>
    <tr>
      <th>Courses</th>
    </tr>
    <CourseListElement
      v-for="cource in courses"
      :key="cource.id"
      :product="cource"
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
