<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" class="form-container">
      <div class="createPost-main-container">
        <el-row>
          <el-col :span="12">
            <el-form-item label-width="120px" style="margin-right: 1rem" label="Project Name:" class="postInfo-container-item">
              <el-select v-model="postForm.Project_name" :disabled="this.isEdit===true?true:false" style="width:100%" class="filter-item" placeholder="Please select">
                <el-option v-for="item in project_name_list" :key="item" :label="item" :value="item" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="4">
            <el-button v-loading="loading" type="success" @click="submitForm">
              Submit
            </el-button>
          </el-col>
          <el-col :span="8">
            <el-form-item label-width="120px" label="Update Month:" class="postInfo-container-item">
              <el-date-picker v-model="postForm.Update" type="month" value-format="yyyy-MM-dd" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <Notice style="margin-bottom: 0px" />
          <el-form-item style="margin-left: 30px">
            <Upload :id="postForm.id" v-model="postForm.Picture" />
          </el-form-item>
          <el-col :span="24">
            <el-form-item prop="title">
              <el-col :span="24">
                <MDinput v-model="postForm.Summary" :maxlength="800" name="Summary" required>
                  Summary Or Comments
                </MDinput>
              </el-col>
            </el-form-item>

            <div class="postInfo-container">
              <el-row>
                <el-col :span="3">
                  <el-form-item label-width="60px" label="COGS:" class="postInfo-container-item">
                    <el-input v-model="postForm.Additional_COGS" :rows="1" type="floatarea" />
                  </el-form-item>
                  <el-form-item label-width="60px" label="PROD:" class="postInfo-container-item">
                    <el-input v-model="postForm.Productivity" :rows="1" type="floatarea" />
                  </el-form-item>
                  <el-form-item label-width="60px" label="CAPEX:" class="postInfo-container-item">
                    <el-input v-model="postForm.CAPEX" :rows="1" type="floatarea" />
                  </el-form-item>
                  <el-form-item label-width="60px" label="Space:" class="postInfo-container-item">
                    <el-input v-model="postForm.Space_needed" :rows="1" type="floatarea" />
                  </el-form-item>
                  <el-form-item label-width="80px" label="Y+3 QTY:" class="postInfo-container-item">
                    <el-input v-model="postForm.Y_3_QTY" :rows="1" type="floatarea" />
                  </el-form-item>
                  <el-form-item label-width="80px" label="Expense:" class="postInfo-container-item">
                    <el-input v-model="postForm.Expense" :rows="1" type="floatarea" />
                  </el-form-item>
                  <el-form-item label-width="80px" label="Payback:" class="postInfo-container-item">
                    <el-input v-model="postForm.Payback" :rows="1" type="floatarea" />
                  </el-form-item>
                </el-col>

                <el-col :span="6">
                  <el-form-item label-width="120px" label="Current Stage:" class="postInfo-container-item">
                    <el-select v-model="postForm.Current_status" class="filter-item" placeholder="Please select">
                      <el-option v-for="item in statusOptions" :key="item" :label="item" :value="item" />
                    </el-select>
                  </el-form-item>
                  <el-form-item label-width="120px" label="Open Time:" class="postInfo-container-item">
                    <el-date-picker v-model="postForm.Open_date" type="month" value-format="yyyy-MM-dd" />
                  </el-form-item>
                  <el-form-item label-width="120px" label="Do Time:" class="postInfo-container-item">
                    <el-date-picker v-model="postForm.Do_date" type="month" value-format="yyyy-MM-dd" />
                  </el-form-item>
                  <el-form-item label-width="120px" label="Imp Time:" class="postInfo-container-item">
                    <el-date-picker v-model="postForm.IMP_date" type="month" value-format="yyyy-MM-dd" />
                  </el-form-item>
                  <el-form-item label-width="120px" label="Produce Time:" class="postInfo-container-item">
                    <el-date-picker v-model="postForm.Produce_date" type="month" value-format="yyyy-MM-dd" />
                  </el-form-item>
                  <el-form-item label-width="120px" label="Sell Time:" class="postInfo-container-item">
                    <el-date-picker v-model="postForm.Sell_date" type="month" value-format="yyyy-MM-dd" />
                  </el-form-item>
                  <el-form-item label-width="120px" label="Close Time:" class="postInfo-container-item">
                    <el-date-picker v-model="postForm.Close_date" type="month" value-format="yyyy-MM-dd" />
                  </el-form-item>
                </el-col>
                <el-col :span="6">
                  <el-form-item style="margin-left: 40px;" label-width="70px" label="Risk1:">
                    <el-input v-model="postForm.Risk1" :rows="1" type="textarea" class="article-textarea" autosize placeholder="Please enter the content" />
                  </el-form-item>
                  <el-form-item style="margin-left: 40px;" label-width="70px" label="Risk2:">
                    <el-input v-model="postForm.Risk2" :rows="1" type="textarea" class="article-textarea" autosize placeholder="Please enter the content" />
                  </el-form-item>
                  <el-form-item style="margin-left: 40px;" label-width="70px" label="Risk3:">
                    <el-input v-model="postForm.Risk3" :rows="1" type="textarea" class="article-textarea" autosize placeholder="Please enter the content" />
                  </el-form-item>
                  <el-form-item style="margin-left: 40px;" label-width="70px" label="Risk4:">
                    <el-input v-model="postForm.Risk4" :rows="1" type="textarea" class="article-textarea" autosize placeholder="Please enter the content" />
                  </el-form-item>
                </el-col>

                <el-col :span="6">
                  <el-form-item style="margin-left: 40px;" label-width="70px" label="Action1:">
                    <el-input v-model="postForm.Action1" :rows="1" type="textarea" class="article-textarea" autosize placeholder="Please enter the content" />
                  </el-form-item>
                  <el-form-item style="margin-left: 40px;" label-width="70px" label="Action2:">
                    <el-input v-model="postForm.Action2" :rows="1" type="textarea" class="article-textarea" autosize placeholder="Please enter the content" />
                  </el-form-item>
                  <el-form-item style="margin-left: 40px;" label-width="70px" label="Action3:">
                    <el-input v-model="postForm.Action3" :rows="1" type="textarea" class="article-textarea" autosize placeholder="Please enter the content" />
                  </el-form-item>
                  <el-form-item style="margin-left: 40px;" label-width="70px" label="Action4:">
                    <el-input v-model="postForm.Action4" :rows="1" type="textarea" class="article-textarea" autosize placeholder="Please enter the content" />
                  </el-form-item>

                </el-col>
              </el-row>
            </div>
          </el-col>
        </el-row>
      </div>
    </el-form>
  </div>
</template>

<script>
import Upload from '@/components/Upload/SingleImage3'
import MDinput from '@/components/MDinput'

import { validURL } from '@/utils/validate'
import { searchUser } from '@/api/remote-search'
import Notice from './Notice'
import { fetchCard, updateCard } from '@/api/card'
import { fetch_search_list } from '@/api/project'

const defaultForm = {
  status: 'draft',
  title: '', // 文章题目
  content: '', // 文章内容
  content_short: '', // 文章摘要
  source_uri: '', // 文章外链
  image_uri: '', // 文章图片
  display_time: undefined, // 前台展示时间
  id: undefined,
  platforms: ['a-platform'],
  comment_disabled: false,
  importance: 0
}

export default {
  name: 'ProjectDetail',
  components: { MDinput, Upload, Notice },
  props: {
    isEdit: {
      type: Boolean,
      default: true
    }
  },
  data() {
    const validateRequire = (rule, value, callback) => {
      if (value === '') {
        this.$message({
          message: rule.field + '为必传项',
          type: 'error'
        })
        callback(new Error(rule.field + '为必传项'))
      } else {
        callback()
      }
    }
    const validateSourceUri = (rule, value, callback) => {
      if (value) {
        if (validURL(value)) {
          callback()
        } else {
          this.$message({
            message: '外链url填写不正确',
            type: 'error'
          })
          callback(new Error('外链url填写不正确'))
        }
      } else {
        callback()
      }
    }
    return {
      postForm: Object.assign({}, defaultForm),
      loading: false,
      userListOptions: [],
      project_name_list: null,
      statusOptions: ['Open', 'Do', 'IMP', 'Produce', 'Sell', 'Closed'],
      rules: {
        // image_uri: [{ validator: validateRequire }],
        title: [{ validator: validateRequire }],
        content: [{ validator: validateRequire }],
        source_uri: [{ validator: validateSourceUri, trigger: 'blur' }]
      },
      tempRoute: {}
    }
  },
  computed: {
    contentShortLength() {
      return this.postForm.content_short.length
    },
    displayTime: {
      // set and get is useful when the data
      // returned by the back end api is different from the front end
      // back end return => "2013-06-25 06:59:25"
      // front end need timestamp => 1372114765000
      get() {
        return (+new Date(this.postForm.display_time))
      },
      set(val) {
        this.postForm.display_time = new Date(val)
      }
    }
  },
  created() {
    if (this.isEdit) {
      const id = this.$route.params && this.$route.params.id
      this.fetchData(id)
    }
    fetch_search_list().then(response => {
      this.project_name_list = response.data.distinct_name
    })

    // Why need to make a copy of this.$route here?
    // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
    // https://github.com/PanJiaChen/vue-element-admin/issues/1221
    this.tempRoute = Object.assign({}, this.$route)
  },
  methods: {
    fetchData(id) {
      fetchCard(id).then(response => {
        this.postForm = response.data
        // set tagsview title
        this.setTagsViewTitle()
        // set page title
        this.setPageTitle()
      }).catch(err => {
        console.log(err.type)
      })
    },
    setTagsViewTitle() {
      const title = 'Edit Project'
      const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.postForm.id}` })
      this.$store.dispatch('tagsView/updateVisitedView', route)
    },
    setPageTitle() {
      const title = 'Edit Card'
      document.title = `${title} - ${this.postForm.id}`
    },
    submitForm() {
      console.log(this.postForm)
      this.$refs.postForm.validate(valid => {
        if (valid) {
          this.loading = true
          updateCard(this.postForm, this.postForm.id).then(() => {
            this.$notify({
              title: 'Success',
              message: 'Update Successfully',
              type: 'success',
              duration: 2000
            })
            this.loading = false
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    getRemoteUserList(query) {
      searchUser(query).then(response => {
        if (!response.data.items) return
        this.userListOptions = response.data.items.map(v => v.name)
      })
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~@/styles/mixin.scss";

.createPost-container {
  position: relative;

  .createPost-main-container {
    padding: 40px 45px 20px 50px;

    .postInfo-container {
      position: relative;
      @include clearfix;
      margin-bottom: 10px;

      .postInfo-container-item {
        float: left;
      }
    }
  }

  .word-counter {
    width: 40px;
    position: absolute;
    right: 10px;
    top: 0px;
  }
}

.article-textarea ::v-deep {
  textarea {
    padding-right: 40px;
    resize: none;
    border: none;
    border-radius: 0px;
    border-bottom: 1px solid #bfcbd9;
  }
}
</style>
