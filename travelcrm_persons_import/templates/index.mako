<%namespace file="travelcrm:templates/common/infoblock.mako" import="infoblock"/>

<div class="dl50 easyui-dialog"
    title="${title}"
    data-options="
        modal:true,
        draggable:false,
        resizable:false,
        iconCls:'fa fa-pencil-square-o',
    ">
    ${h.tags.form(
        request.url, 
        class_="_ajax %s" % ('readonly' if readonly else ''), 
        autocomplete="off",
        multipart=True,
        hidden_fields=[('csrf_token', request.session.get_csrf_token())]
    )}

        ${infoblock(_(u"Upload CSV file and set column numbers for fields"))}
    
        <div class="form-field mt05">
            <div class="dl15">
                ${h.tags.title(_(u"file"), True, "file")}
            </div>
            <div class="ml15">
                ${h.tags.text(
                    'file', None, class_='easyui-filebox w20',
                    data_options="buttonText: '%s'" % _(u'Choose File')
                )}
                ${h.common.error_container(name='file')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"first name"), True, "first_name")}
            </div>
            <div class="ml15">
                ${h.tags.text(
                    'first_name', 0, class_='easyui-numberspinner w10',
                    data_options="min:0,max:100,editable:false"
                )}
                ${h.common.error_container(name='first_name')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"second name"), False, "second_name")}
            </div>
            <div class="ml15">
                ${h.tags.text(
                    'second_name', 0, class_='easyui-numberspinner w10',
                    data_options="min:0,max:100,editable:false"
                )}
                ${h.common.error_container(name='second_name')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"last name"), True, "last_name")}
            </div>
            <div class="ml15">
                ${h.tags.text('last_name', 0, class_='easyui-numberspinner w10', data_options="min:0,max:100,editable:false")}
                ${h.common.error_container(name='last_name')}
            </div>
        </div>
        <div class="form-field">
            <div class="dl15">
                ${h.tags.title(_(u"phones"), False, "phones")}
            </div>
            <div class="ml15">
                ${h.tags.text('phones', 0, class_='easyui-numberspinner w10', data_options="min:0,max:100,editable:false")}
                ${h.common.error_container(name='phones')}
            </div>
        </div>
        <div class="form-field mb05">
            <div class="dl15">
                ${h.tags.title(_(u"emails"), False, "emails")}
            </div>
            <div class="ml15">
                ${h.tags.text('emails', 0, class_='easyui-numberspinner w10', data_options="min:0,max:100,editable:false")}
                ${h.common.error_container(name='emails')}
            </div>
        </div>
        <div class="easyui-tabs" data-options="border:false,height:170">
            <div title="${_(u'Passport')}">
                <div class="form-field">
                    <div class="dl15">
                        ${h.tags.title(_(u"country"), True, "passport_country")}
                    </div>
                    <div class="ml15">
                        ${h.tags.text('passport_country', 0, class_='easyui-numberspinner w10', data_options="min:0,max:100,editable:false")}
                        ${h.common.error_container(name='passport_country')}
                    </div>
                </div>
                <div class="form-field">
                    <div class="dl15">
                        ${h.tags.title(_(u"num"), True, "passport_num")}
                    </div>
                    <div class="ml15">
                        ${h.tags.text('passport_num', 0, class_='easyui-numberspinner w10', data_options="min:0,max:100,editable:false")}
                        ${h.common.error_container(name='passport_num')}
                    </div>
                </div>
                <div class="form-field">
                    <div class="dl15">
                        ${h.tags.title(_(u"description"), False, "passport_description")}
                    </div>
                    <div class="ml15">
                        ${h.tags.text('passport_description', 0, class_='easyui-numberspinner w10', data_options="min:0,max:100,editable:false")}
                        ${h.common.error_container(name='passport_description')}
                    </div>
                </div>
            </div>
            <div title="${_(u'Foreign Passport')}">
                <div class="form-field">
                    <div class="dl15">
                        ${h.tags.title(_(u"country"), True, "foreign_passport_country")}
                    </div>
                    <div class="ml15">
                        ${h.tags.text('foreign_passport_country', 0, class_='easyui-numberspinner w10', data_options="min:0,max:100,editable:false")}
                        ${h.common.error_container(name='foreign_passport_country')}
                    </div>
                </div>
                <div class="form-field">
                    <div class="dl15">
                        ${h.tags.title(_(u"num"), True, "foreign_passport_num")}
                    </div>
                    <div class="ml15">
                        ${h.tags.text('foreign_passport_num', 0, class_='easyui-numberspinner w10', data_options="min:0,max:100,editable:false")}
                        ${h.common.error_container(name='foreign_passport_num')}
                    </div>
                </div>
                <div class="form-field">
                    <div class="dl15">
                        ${h.tags.title(_(u"end date"), True, "foreign_passport_end_date")}
                    </div>
                    <div class="ml15">
                        ${h.tags.text('foreign_passport_end_date', 0, class_='easyui-numberspinner w10', data_options="min:0,max:100,editable:false")}
                        ${h.common.error_container(name='foreign_passport_end_date')}
                    </div>
                </div>
                <div class="form-field">
                    <div class="dl15">
                        ${h.tags.title(_(u"description"), False, "foreign_passport_description")}
                    </div>
                    <div class="ml15">
                        ${h.tags.text('foreign_passport_description', 0, class_='easyui-numberspinner w10', data_options="min:0,max:100,editable:false")}
                        ${h.common.error_container(name='foreign_passport_description')}
                    </div>
                </div>
            </div>
        </div>
        <div class="form-buttons">
            <div class="dl20 status-bar"></div>
            <div class="ml20 tr button-group">
                ${h.tags.submit('save', _(u"Import"), class_="button easyui-linkbutton")}
                ${h.common.reset('cancel', _(u"Cancel"), class_="button danger easyui-linkbutton")}
            </div>
        </div>
    ${h.tags.end_form()}
</div>
