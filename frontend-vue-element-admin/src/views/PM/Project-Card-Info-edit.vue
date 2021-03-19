<template>
  <project-detail :is-edit="true" />
</template>

<script>
import ProjectDetail from './components/ProjectDetail'

export default {
  name: 'EditForm',
  components: { ProjectDetail }
}
</script>

