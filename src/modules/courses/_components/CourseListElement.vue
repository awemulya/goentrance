<template>
  <tr>
    <td><router-link :to="{ name: 'Subject', params: { courseId: course.id }}">{{course.name}}</router-link></td>
  </tr>
</template>

<script>
export default {
  name: 'CoursetListElement',
  props: {
    course: {
      type: Object
    }
  }
}
</script>
