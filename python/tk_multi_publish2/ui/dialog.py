# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 588)
        self.verticalLayout_7 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.main_stack = QtGui.QStackedWidget(Dialog)
        self.main_stack.setObjectName("main_stack")
        self.large_drop_area_frame = QtGui.QWidget()
        self.large_drop_area_frame.setObjectName("large_drop_area_frame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.large_drop_area_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.large_drop_area = DropAreaFrame(self.large_drop_area_frame)
        self.large_drop_area.setFrameShape(QtGui.QFrame.StyledPanel)
        self.large_drop_area.setFrameShadow(QtGui.QFrame.Raised)
        self.large_drop_area.setObjectName("large_drop_area")
        self.gridLayout_2 = QtGui.QGridLayout(self.large_drop_area)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 98, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(166, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtGui.QLabel(self.large_drop_area)
        self.label_5.setMinimumSize(QtCore.QSize(150, 150))
        self.label_5.setMaximumSize(QtCore.QSize(150, 150))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/tk_multi_publish2/icon_256.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.large_drop_area_label = QtGui.QLabel(self.large_drop_area)
        self.large_drop_area_label.setStyleSheet("QLabel {\n"
"    font-size: 24px;\n"
"}")
        self.large_drop_area_label.setAlignment(QtCore.Qt.AlignCenter)
        self.large_drop_area_label.setObjectName("large_drop_area_label")
        self.verticalLayout.addWidget(self.large_drop_area_label)
        spacerItem3 = QtGui.QSpacerItem(0, 12, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label = QtGui.QLabel(self.large_drop_area)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem4 = QtGui.QSpacerItem(0, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.drop_area_browse_file = QtGui.QToolButton(self.large_drop_area)
        self.drop_area_browse_file.setMinimumSize(QtCore.QSize(160, 85))
        self.drop_area_browse_file.setMaximumSize(QtCore.QSize(150, 85))
        self.drop_area_browse_file.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drop_area_browse_file.setIcon(icon)
        self.drop_area_browse_file.setIconSize(QtCore.QSize(32, 32))
        self.drop_area_browse_file.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.drop_area_browse_file.setObjectName("drop_area_browse_file")
        self.horizontalLayout_3.addWidget(self.drop_area_browse_file)
        spacerItem6 = QtGui.QSpacerItem(12, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.drop_area_browse_seq = QtGui.QToolButton(self.large_drop_area)
        self.drop_area_browse_seq.setMinimumSize(QtCore.QSize(160, 85))
        self.drop_area_browse_seq.setMaximumSize(QtCore.QSize(150, 85))
        self.drop_area_browse_seq.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/image_sequence.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drop_area_browse_seq.setIcon(icon1)
        self.drop_area_browse_seq.setIconSize(QtCore.QSize(32, 32))
        self.drop_area_browse_seq.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.drop_area_browse_seq.setObjectName("drop_area_browse_seq")
        self.horizontalLayout_3.addWidget(self.drop_area_browse_seq)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.drag_progress_message = QtGui.QPushButton(self.large_drop_area)
        self.drag_progress_message.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/status_warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drag_progress_message.setIcon(icon2)
        self.drag_progress_message.setIconSize(QtCore.QSize(22, 22))
        self.drag_progress_message.setFlat(True)
        self.drag_progress_message.setObjectName("drag_progress_message")
        self.horizontalLayout_4.addWidget(self.drag_progress_message)
        spacerItem10 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(6, 10)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(179, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 1, 2, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(20, 213, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem12, 2, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setRowStretch(0, 3)
        self.gridLayout_2.setRowStretch(2, 4)
        self.verticalLayout_3.addWidget(self.large_drop_area)
        self.main_stack.addWidget(self.large_drop_area_frame)
        self.main_ui_frame = QtGui.QWidget()
        self.main_ui_frame.setObjectName("main_ui_frame")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.main_ui_frame)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.main_frame = QtGui.QWidget(self.main_ui_frame)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.main_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.splitter = QtGui.QSplitter(self.main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = DropAreaFrame(self.splitter)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.items_tree = PublishTreeWidget(self.frame)
        self.items_tree.setAcceptDrops(True)
        self.items_tree.setDragEnabled(True)
        self.items_tree.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.items_tree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.items_tree.setObjectName("items_tree")
        self.items_tree.headerItem().setText(0, "1")
        self.items_tree.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.items_tree)
        self.text_below_item_tree = QtGui.QLabel(self.frame)
        self.text_below_item_tree.setAlignment(QtCore.Qt.AlignCenter)
        self.text_below_item_tree.setObjectName("text_below_item_tree")
        self.verticalLayout_2.addWidget(self.text_below_item_tree)
        self.details_frame = QtGui.QFrame(self.splitter)
        self.details_frame.setObjectName("details_frame")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.details_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.details_stack = QtGui.QStackedWidget(self.details_frame)
        self.details_stack.setObjectName("details_stack")
        self.details_item = QtGui.QWidget()
        self.details_item.setObjectName("details_item")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.details_item)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setContentsMargins(8, 0, 8, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.item_icon = QtGui.QLabel(self.details_item)
        self.item_icon.setMinimumSize(QtCore.QSize(60, 60))
        self.item_icon.setMaximumSize(QtCore.QSize(60, 60))
        self.item_icon.setText("")
        self.item_icon.setScaledContents(True)
        self.item_icon.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.item_icon.setObjectName("item_icon")
        self.horizontalLayout_2.addWidget(self.item_icon)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.item_name = ElidedLabel(self.details_item)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_name.sizePolicy().hasHeightForWidth())
        self.item_name.setSizePolicy(sizePolicy)
        self.item_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.item_name.setObjectName("item_name")
        self.verticalLayout_12.addWidget(self.item_name)
        self.item_type = QtGui.QLabel(self.details_item)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_type.sizePolicy().hasHeightForWidth())
        self.item_type.setSizePolicy(sizePolicy)
        self.item_type.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.item_type.setObjectName("item_type")
        self.verticalLayout_12.addWidget(self.item_type)
        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.item_divider_1 = QtGui.QFrame(self.details_item)
        self.item_divider_1.setFrameShape(QtGui.QFrame.HLine)
        self.item_divider_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.item_divider_1.setObjectName("item_divider_1")
        self.verticalLayout_6.addWidget(self.item_divider_1)
        self.context_widget = ContextWidget(self.details_item)
        self.context_widget.setObjectName("context_widget")
        self.verticalLayout_6.addWidget(self.context_widget)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setVerticalSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.item_inherited_item_label = QtGui.QLabel(self.details_item)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_inherited_item_label.sizePolicy().hasHeightForWidth())
        self.item_inherited_item_label.setSizePolicy(sizePolicy)
        self.item_inherited_item_label.setStyleSheet("")
        self.item_inherited_item_label.setWordWrap(True)
        self.item_inherited_item_label.setIndent(5)
        self.item_inherited_item_label.setOpenExternalLinks(False)
        self.item_inherited_item_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.item_inherited_item_label.setObjectName("item_inherited_item_label")
        self.gridLayout_3.addWidget(self.item_inherited_item_label, 2, 1, 1, 1)
        self.item_thumbnail_label = QtGui.QLabel(self.details_item)
        self.item_thumbnail_label.setObjectName("item_thumbnail_label")
        self.gridLayout_3.addWidget(self.item_thumbnail_label, 0, 2, 1, 1)
        self.item_thumbnail = Thumbnail(self.details_item)
        self.item_thumbnail.setMinimumSize(QtCore.QSize(160, 90))
        self.item_thumbnail.setMaximumSize(QtCore.QSize(160, 90))
        self.item_thumbnail.setText("")
        self.item_thumbnail.setScaledContents(False)
        self.item_thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.item_thumbnail.setObjectName("item_thumbnail")
        self.gridLayout_3.addWidget(self.item_thumbnail, 1, 2, 1, 1)
        self.item_description_label = QtGui.QLabel(self.details_item)
        self.item_description_label.setObjectName("item_description_label")
        self.gridLayout_3.addWidget(self.item_description_label, 0, 1, 1, 1)
        self.item_comments = PublishDescriptionEdit(self.details_item)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_comments.sizePolicy().hasHeightForWidth())
        self.item_comments.setSizePolicy(sizePolicy)
        self.item_comments.setMinimumSize(QtCore.QSize(0, 90))
        self.item_comments.setMaximumSize(QtCore.QSize(16777215, 90))
        self.item_comments.setObjectName("item_comments")
        self.gridLayout_3.addWidget(self.item_comments, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.item_summary_label = QtGui.QLabel(self.details_item)
        self.item_summary_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.item_summary_label.setObjectName("item_summary_label")
        self.verticalLayout_6.addWidget(self.item_summary_label)
        self.scrollArea = QtGui.QScrollArea(self.details_item)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 408, 97))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.item_summary = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.item_summary.setText("")
        self.item_summary.setWordWrap(True)
        self.item_summary.setObjectName("item_summary")
        self.verticalLayout_10.addWidget(self.item_summary)
        self.expander_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.expander_label.setText("")
        self.expander_label.setOpenExternalLinks(False)
        self.expander_label.setObjectName("expander_label")
        self.verticalLayout_10.addWidget(self.expander_label)
        self.verticalLayout_10.setStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.item_settings_label = QtGui.QLabel(self.details_item)
        self.item_settings_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.item_settings_label.setObjectName("item_settings_label")
        self.verticalLayout_6.addWidget(self.item_settings_label)
        self.item_settings = SettingsWidget(self.details_item)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_settings.sizePolicy().hasHeightForWidth())
        self.item_settings.setSizePolicy(sizePolicy)
        self.item_settings.setObjectName("item_settings")
        self.verticalLayout_6.addWidget(self.item_settings)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(3, 1)
        self.verticalLayout_6.setStretch(4, 1)
        self.verticalLayout_6.setStretch(5, 5)
        self.verticalLayout_6.setStretch(6, 1)
        self.verticalLayout_6.setStretch(7, 5)
        self.details_stack.addWidget(self.details_item)
        self.details_task = QtGui.QWidget()
        self.details_task.setObjectName("details_task")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.details_task)
        self.verticalLayout_11.setSpacing(8)
        self.verticalLayout_11.setContentsMargins(8, 0, 8, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.task_header_layout = QtGui.QHBoxLayout()
        self.task_header_layout.setObjectName("task_header_layout")
        self.task_icon = QtGui.QLabel(self.details_task)
        self.task_icon.setMinimumSize(QtCore.QSize(60, 60))
        self.task_icon.setMaximumSize(QtCore.QSize(60, 60))
        self.task_icon.setText("")
        self.task_icon.setScaledContents(True)
        self.task_icon.setObjectName("task_icon")
        self.task_header_layout.addWidget(self.task_icon)
        self.task_name = QtGui.QLabel(self.details_task)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_name.sizePolicy().hasHeightForWidth())
        self.task_name.setSizePolicy(sizePolicy)
        self.task_name.setObjectName("task_name")
        self.task_header_layout.addWidget(self.task_name)
        self.verticalLayout_11.addLayout(self.task_header_layout)
        self.task_settings_scroll_area = QtGui.QScrollArea(self.details_task)
        self.task_settings_scroll_area.setWidgetResizable(True)
        self.task_settings_scroll_area.setObjectName("task_settings_scroll_area")
        self.task_settings_parent = QtGui.QWidget()
        self.task_settings_parent.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.task_settings_parent.setObjectName("task_settings_parent")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.task_settings_parent)
        self.verticalLayout_13.setSpacing(-1)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.task_settings = CustomSettingsWidget(self.task_settings_parent)
        self.task_settings.setObjectName("task_settings")
        self.verticalLayout_13.addWidget(self.task_settings)
        spacerItem13 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem13)
        self.verticalLayout_13.setStretch(1, 10)
        self.task_settings_scroll_area.setWidget(self.task_settings_parent)
        self.verticalLayout_11.addWidget(self.task_settings_scroll_area)
        self.details_stack.addWidget(self.details_task)
        self.details_please_select = QtGui.QWidget()
        self.details_please_select.setObjectName("details_please_select")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.details_please_select)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setContentsMargins(8, 0, 8, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.please_select_an_item = QtGui.QLabel(self.details_please_select)
        self.please_select_an_item.setAlignment(QtCore.Qt.AlignCenter)
        self.please_select_an_item.setObjectName("please_select_an_item")
        self.verticalLayout_8.addWidget(self.please_select_an_item)
        self.details_stack.addWidget(self.details_please_select)
        self.details_multi_edit_not_supported = QtGui.QWidget()
        self.details_multi_edit_not_supported.setObjectName("details_multi_edit_not_supported")
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.details_multi_edit_not_supported)
        self.verticalLayout_15.setSpacing(8)
        self.verticalLayout_15.setContentsMargins(8, 0, 8, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_2 = QtGui.QLabel(self.details_multi_edit_not_supported)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_15.addWidget(self.label_2)
        self.details_stack.addWidget(self.details_multi_edit_not_supported)
        self.verticalLayout_5.addWidget(self.details_stack)
        self.verticalLayout_9.addWidget(self.splitter)
        self.verticalLayout_4.addWidget(self.main_frame)
        self.progress_bar = QtGui.QProgressBar(self.main_ui_frame)
        self.progress_bar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout_4.addWidget(self.progress_bar)
        self.bottom_frame = QtGui.QFrame(self.main_ui_frame)
        self.bottom_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.bottom_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.bottom_frame)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(2, 8, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_container = QtGui.QWidget(self.bottom_frame)
        self.button_container.setObjectName("button_container")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.button_container)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.browse = QtGui.QToolButton(self.button_container)
        self.browse.setMaximumSize(QtCore.QSize(32, 32))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/browse_menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browse.setIcon(icon3)
        self.browse.setIconSize(QtCore.QSize(32, 32))
        self.browse.setObjectName("browse")
        self.horizontalLayout_5.addWidget(self.browse)
        self.refresh = QtGui.QToolButton(self.button_container)
        self.refresh.setMaximumSize(QtCore.QSize(32, 32))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh.setIcon(icon4)
        self.refresh.setIconSize(QtCore.QSize(32, 32))
        self.refresh.setObjectName("refresh")
        self.horizontalLayout_5.addWidget(self.refresh)
        self.delete_items = QtGui.QToolButton(self.button_container)
        self.delete_items.setMaximumSize(QtCore.QSize(32, 32))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_items.setIcon(icon5)
        self.delete_items.setIconSize(QtCore.QSize(32, 32))
        self.delete_items.setObjectName("delete_items")
        self.horizontalLayout_5.addWidget(self.delete_items)
        self.expand_all = QtGui.QToolButton(self.button_container)
        self.expand_all.setMaximumSize(QtCore.QSize(32, 32))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/expand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expand_all.setIcon(icon6)
        self.expand_all.setIconSize(QtCore.QSize(32, 32))
        self.expand_all.setObjectName("expand_all")
        self.horizontalLayout_5.addWidget(self.expand_all)
        self.collapse_all = QtGui.QToolButton(self.button_container)
        self.collapse_all.setMaximumSize(QtCore.QSize(32, 32))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/contract.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.collapse_all.setIcon(icon7)
        self.collapse_all.setIconSize(QtCore.QSize(32, 32))
        self.collapse_all.setObjectName("collapse_all")
        self.horizontalLayout_5.addWidget(self.collapse_all)
        self.help = QtGui.QToolButton(self.button_container)
        self.help.setMinimumSize(QtCore.QSize(32, 32))
        self.help.setMaximumSize(QtCore.QSize(32, 32))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon8)
        self.help.setIconSize(QtCore.QSize(32, 32))
        self.help.setObjectName("help")
        self.horizontalLayout_5.addWidget(self.help)
        self.horizontalLayout.addWidget(self.button_container)
        spacerItem14 = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.progress_status_icon = QtGui.QLabel(self.bottom_frame)
        self.progress_status_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.progress_status_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.progress_status_icon.setText("")
        self.progress_status_icon.setPixmap(QtGui.QPixmap(":/tk_multi_publish2/status_success.png"))
        self.progress_status_icon.setScaledContents(True)
        self.progress_status_icon.setObjectName("progress_status_icon")
        self.horizontalLayout.addWidget(self.progress_status_icon)
        self.progress_message = ProgressStatusLabel(self.bottom_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_message.sizePolicy().hasHeightForWidth())
        self.progress_message.setSizePolicy(sizePolicy)
        self.progress_message.setObjectName("progress_message")
        self.horizontalLayout.addWidget(self.progress_message)
        self.stop_processing = QtGui.QToolButton(self.bottom_frame)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/tk_multi_publish2/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_processing.setIcon(icon9)
        self.stop_processing.setIconSize(QtCore.QSize(20, 20))
        self.stop_processing.setObjectName("stop_processing")
        self.horizontalLayout.addWidget(self.stop_processing)
        self.validate = QtGui.QPushButton(self.bottom_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validate.sizePolicy().hasHeightForWidth())
        self.validate.setSizePolicy(sizePolicy)
        self.validate.setObjectName("validate")
        self.horizontalLayout.addWidget(self.validate)
        self.publish = QtGui.QPushButton(self.bottom_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.publish.sizePolicy().hasHeightForWidth())
        self.publish.setSizePolicy(sizePolicy)
        self.publish.setObjectName("publish")
        self.horizontalLayout.addWidget(self.publish)
        self.close = QtGui.QPushButton(self.bottom_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy)
        self.close.setObjectName("close")
        self.horizontalLayout.addWidget(self.close)
        self.verticalLayout_4.addWidget(self.bottom_frame)
        self.main_stack.addWidget(self.main_ui_frame)
        self.verticalLayout_7.addWidget(self.main_stack)

        self.retranslateUi(Dialog)
        self.main_stack.setCurrentIndex(1)
        self.details_stack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.validate, self.publish)
        Dialog.setTabOrder(self.publish, self.items_tree)
        Dialog.setTabOrder(self.items_tree, self.close)
        Dialog.setTabOrder(self.close, self.stop_processing)
        Dialog.setTabOrder(self.stop_processing, self.scrollArea)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Shotgun Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.large_drop_area_label.setText(QtGui.QApplication.translate("Dialog", "Drag and drop files or folders here", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Or, if you prefer...", None, QtGui.QApplication.UnicodeUTF8))
        self.drop_area_browse_file.setToolTip(QtGui.QApplication.translate("Dialog", "Browse files to publish", None, QtGui.QApplication.UnicodeUTF8))
        self.drop_area_browse_file.setText(QtGui.QApplication.translate("Dialog", "Browse files to publish\n"
"    ", None, QtGui.QApplication.UnicodeUTF8))
        self.drop_area_browse_seq.setToolTip(QtGui.QApplication.translate("Dialog", "Browse sequences to publish", None, QtGui.QApplication.UnicodeUTF8))
        self.drop_area_browse_seq.setText(QtGui.QApplication.translate("Dialog", "Browse folders to publish\n"
"image sequences", None, QtGui.QApplication.UnicodeUTF8))
        self.drag_progress_message.setText(QtGui.QApplication.translate("Dialog", "Click for more info...", None, QtGui.QApplication.UnicodeUTF8))
        self.text_below_item_tree.setText(QtGui.QApplication.translate("Dialog", "Drag and drop items here to add them. ", None, QtGui.QApplication.UnicodeUTF8))
        self.item_name.setText(QtGui.QApplication.translate("Dialog", "Item name", None, QtGui.QApplication.UnicodeUTF8))
        self.item_type.setText(QtGui.QApplication.translate("Dialog", "Item type", None, QtGui.QApplication.UnicodeUTF8))
        self.item_inherited_item_label.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Inherited from: test</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.item_thumbnail_label.setText(QtGui.QApplication.translate("Dialog", "Thumbnail:", None, QtGui.QApplication.UnicodeUTF8))
        self.item_thumbnail.setToolTip(QtGui.QApplication.translate("Dialog", "Click to take a screenshot.", None, QtGui.QApplication.UnicodeUTF8))
        self.item_description_label.setText(QtGui.QApplication.translate("Dialog", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.item_summary_label.setText(QtGui.QApplication.translate("Dialog", "Summary:", None, QtGui.QApplication.UnicodeUTF8))
        self.item_settings_label.setText(QtGui.QApplication.translate("Dialog", "Settings:", None, QtGui.QApplication.UnicodeUTF8))
        self.task_name.setText(QtGui.QApplication.translate("Dialog", "Task Name", None, QtGui.QApplication.UnicodeUTF8))
        self.please_select_an_item.setText(QtGui.QApplication.translate("Dialog", "Please select tasks of the same type or a single item.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Multiple selection not supported on tasks of this type.\n"
"Please select a single task.", None, QtGui.QApplication.UnicodeUTF8))
        self.browse.setToolTip(QtGui.QApplication.translate("Dialog", "<p>Click this button to browse files for publishing. You can also click and hold the button to show the full browsing menu which includes an option to browse folders to publish image sequences.</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.browse.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh.setToolTip(QtGui.QApplication.translate("Dialog", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_items.setToolTip(QtGui.QApplication.translate("Dialog", "Delete selected items", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_items.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.expand_all.setToolTip(QtGui.QApplication.translate("Dialog", "Expand all items", None, QtGui.QApplication.UnicodeUTF8))
        self.expand_all.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.collapse_all.setToolTip(QtGui.QApplication.translate("Dialog", "Collapse all items", None, QtGui.QApplication.UnicodeUTF8))
        self.collapse_all.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.help.setToolTip(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Open documentation for the publish workflow.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.help.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.progress_message.setText(QtGui.QApplication.translate("Dialog", "Progress message....", None, QtGui.QApplication.UnicodeUTF8))
        self.stop_processing.setToolTip(QtGui.QApplication.translate("Dialog", "Stop Processing", None, QtGui.QApplication.UnicodeUTF8))
        self.stop_processing.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.validate.setText(QtGui.QApplication.translate("Dialog", "Validate", None, QtGui.QApplication.UnicodeUTF8))
        self.publish.setText(QtGui.QApplication.translate("Dialog", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

from ..thumbnail import Thumbnail
from ..progress_status_label import ProgressStatusLabel
from ..publish_description_edit import PublishDescriptionEdit
from ..custom_settings_widget import CustomSettingsWidget
from ..publish_tree_widget import PublishTreeWidget
from ..settings_widget import SettingsWidget
from ..drop_area import DropAreaFrame
from ..qtwidgets import ElidedLabel, ContextWidget
from . import resources_rc
