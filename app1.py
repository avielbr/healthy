from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import json


class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)
        self.URL = "https://health.jce.ac.il/eforms/%d7%94%d7%a6%d7%94%d7%a8%d7%aa-%d7%91%d7%a8%d7%99%d7%90%d7%95%d7%aa/53/"
        self.DETAILS = json.load(open('details.json'))

    def do_it(self):
        self.driver.get(self.URL)
        sleep(1)

        last_name_box = self.driver.find_element_by_css_selector("body.rtl.blog.custom-background.ipt_uif_common:nth-child(2) div.ipt_uif_front.ipt_uif_common.ipt_fsqm_form.type_0.ui-front.eform-rtl.eform-override-element-material.eform-override-alignment-inherit.ipt-uif-custom-material-red:nth-child(2) div.ipt_uif_hidden_init:nth-child(7) form.ipt_uif_validate_form.ipt_fsqm_main_form div.ipt-eform-width-restrain:nth-child(7) div.ipt-eform-content.ipt-eform-no-wrap div.ipt-eform-layout-wrapper:nth-child(1) div.ipt_uif_column.ipt_uif_column_half.ipt_uif_conditional.ipt_uif_column_custom.ipt_fsqm_container_col_half:nth-child(7) div.ipt_uif_column_inner div.ipt_uif_column.ipt_uif_column_full.ipt_uif_conditional.ipt_fsqm_container_l_name:nth-child(3) div.ipt_uif_column_inner.side_margin div.ipt_uif_question.ipt_uif_question_full div.ipt_uif_question_content div.input-field.has-icon > label:nth-child(3)")
        first_name_box = self.driver.find_element_by_css_selector("body.rtl.blog.custom-background.ipt_uif_common:nth-child(2) div.ipt_uif_front.ipt_uif_common.ipt_fsqm_form.type_0.ui-front.eform-rtl.eform-override-element-material.eform-override-alignment-inherit.ipt-uif-custom-material-red:nth-child(2) div.ipt_uif_hidden_init:nth-child(7) form.ipt_uif_validate_form.ipt_fsqm_main_form div.ipt-eform-width-restrain:nth-child(7) div.ipt-eform-content.ipt-eform-no-wrap div.ipt-eform-layout-wrapper:nth-child(1) div.ipt_uif_column.ipt_uif_column_half.ipt_uif_conditional.ipt_uif_column_custom.ipt_fsqm_container_col_half:nth-child(7) div.ipt_uif_column_inner div.ipt_uif_column.ipt_uif_column_full.ipt_uif_conditional.ipt_fsqm_container_f_name:nth-child(6) div.ipt_uif_column_inner.side_margin div.ipt_uif_question.ipt_uif_question_full div.ipt_uif_question_content div.input-field.has-icon > label:nth-child(3)")
        email_box = self.driver.find_element_by_css_selector("body.rtl.blog.custom-background.ipt_uif_common:nth-child(2) div.ipt_uif_front.ipt_uif_common.ipt_fsqm_form.type_0.ui-front.eform-rtl.eform-override-element-material.eform-override-alignment-inherit.ipt-uif-custom-material-red:nth-child(2) div.ipt_uif_hidden_init:nth-child(7) form.ipt_uif_validate_form.ipt_fsqm_main_form div.ipt-eform-width-restrain:nth-child(7) div.ipt-eform-content.ipt-eform-no-wrap div.ipt-eform-layout-wrapper:nth-child(1) div.ipt_uif_column.ipt_uif_column_half.ipt_uif_conditional.ipt_uif_column_custom.ipt_fsqm_container_col_half:nth-child(10) div.ipt_uif_column_inner div.ipt_uif_column.ipt_uif_column_full.ipt_uif_conditional.ipt_fsqm_container_email:nth-child(3) div.ipt_uif_column_inner.side_margin div.ipt_uif_question.ipt_uif_question_full div.ipt_uif_question_content div.input-field.has-icon > label:nth-child(3)")
        i_declare = self.driver.find_element_by_css_selector("body.rtl.blog.custom-background.ipt_uif_common:nth-child(2) div.ipt_uif_front.ipt_uif_common.ipt_fsqm_form.type_0.ui-front.eform-rtl.eform-override-element-material.eform-override-alignment-inherit.ipt-uif-custom-material-red:nth-child(2) div.ipt_uif_hidden_init:nth-child(7) form.ipt_uif_validate_form.ipt_fsqm_main_form div.ipt-eform-width-restrain:nth-child(7) div.ipt-eform-content.ipt-eform-no-wrap div.ipt_fsqm_terms_wrap.ui-widget-content:nth-child(2) div.ipt_uif_column.ipt_uif_column_full.ipt_uif_conditional div.ipt_uif_column_inner.side_margin div.ipt_uif_label_column.column_1:nth-child(1) > label.eform-label-with-tabindex")
        student = self.driver.find_element_by_css_selector("body.rtl.blog.custom-background.ipt_uif_common:nth-child(2) div.ipt_uif_front.ipt_uif_common.ipt_fsqm_form.type_0.ui-front.eform-rtl.eform-override-element-material.eform-override-alignment-inherit.ipt-uif-custom-material-red:nth-child(2) div.ipt_uif_hidden_init:nth-child(7) form.ipt_uif_validate_form.ipt_fsqm_main_form div.ipt-eform-width-restrain:nth-child(7) div.ipt-eform-content.ipt-eform-no-wrap div.ipt-eform-layout-wrapper:nth-child(1) div.ipt_uif_column.ipt_uif_column_half.ipt_uif_conditional.ipt_uif_column_custom.ipt_fsqm_container_col_half:nth-child(10) div.ipt_uif_column_inner div.ipt_uif_column.ipt_uif_column_full.ipt_uif_conditional.ipt_fsqm_container_radio:nth-child(6) div.ipt_uif_column_inner.side_margin div.ipt_uif_question div.ipt_uif_question_content div.ipt_uif_label_column.column_3:nth-child(2) > label.eform-label-with-tabindex")
        send = self.driver.find_element_by_name("ipt_fsqm_form_53_button_submit")

        self.actions.click(last_name_box)
        self.actions.send_keys(self.DETAILS['last'])
        self.actions.click(first_name_box)
        self.actions.send_keys(self.DETAILS['first'])
        self.actions.click(email_box)
        self.actions.send_keys(self.DETAILS['email'])
        self.actions.click(student)
        self.actions.click(i_declare)
        self.actions.click(send).perform()


runner = Browser()
runner.do_it()
