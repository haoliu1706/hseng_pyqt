# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acc_info.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(955, 296)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget_acc_info = QtWidgets.QTabWidget(Form)
        self.tabWidget_acc_info.setObjectName("tabWidget_acc_info")
        self.tab_orders = QtWidgets.QWidget()
        self.tab_orders.setObjectName("tab_orders")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_orders)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget_orders = QtWidgets.QTableWidget(self.tab_orders)
        self.tableWidget_orders.setObjectName("tableWidget_orders")
        self.tableWidget_orders.setColumnCount(14)
        self.tableWidget_orders.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_orders.setHorizontalHeaderItem(13, item)
        self.tableWidget_orders.horizontalHeader().setDefaultSectionSize(65)
        self.tableWidget_orders.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_orders.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_2.addWidget(self.tableWidget_orders)
        self.tabWidget_acc_info.addTab(self.tab_orders, "")
        self.tab_pos = QtWidgets.QWidget()
        self.tab_pos.setObjectName("tab_pos")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_pos)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget_pos = QtWidgets.QTableWidget(self.tab_pos)
        self.tableWidget_pos.setObjectName("tableWidget_pos")
        self.tableWidget_pos.setColumnCount(14)
        self.tableWidget_pos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_pos.setHorizontalHeaderItem(13, item)
        self.tableWidget_pos.horizontalHeader().setDefaultSectionSize(65)
        self.tableWidget_pos.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_pos.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_3.addWidget(self.tableWidget_pos)
        self.tabWidget_acc_info.addTab(self.tab_pos, "")
        self.tab_trades = QtWidgets.QWidget()
        self.tab_trades.setObjectName("tab_trades")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_trades)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget_trades = QtWidgets.QTableWidget(self.tab_trades)
        self.tableWidget_trades.setObjectName("tableWidget_trades")
        self.tableWidget_trades.setColumnCount(14)
        self.tableWidget_trades.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_trades.setHorizontalHeaderItem(13, item)
        self.tableWidget_trades.horizontalHeader().setDefaultSectionSize(65)
        self.tableWidget_trades.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_trades.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_4.addWidget(self.tableWidget_trades)
        self.tabWidget_acc_info.addTab(self.tab_trades, "")
        self.tab_bal = QtWidgets.QWidget()
        self.tab_bal.setObjectName("tab_bal")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_bal)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidget_bal = QtWidgets.QTableWidget(self.tab_bal)
        self.tableWidget_bal.setObjectName("tableWidget_bal")
        self.tableWidget_bal.setColumnCount(8)
        self.tableWidget_bal.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bal.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bal.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bal.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bal.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bal.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bal.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bal.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bal.setHorizontalHeaderItem(7, item)
        self.tableWidget_bal.horizontalHeader().setDefaultSectionSize(65)
        self.tableWidget_bal.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_bal.horizontalHeader().setStretchLastSection(False)
        self.horizontalLayout_5.addWidget(self.tableWidget_bal)
        self.tabWidget_acc_info.addTab(self.tab_bal, "")
        self.tab_ccy = QtWidgets.QWidget()
        self.tab_ccy.setObjectName("tab_ccy")
        self.tabWidget_acc_info.addTab(self.tab_ccy, "")
        self.horizontalLayout.addWidget(self.tabWidget_acc_info)

        self.retranslateUi(Form)
        self.tabWidget_acc_info.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget_orders.horizontalHeaderItem(0)
        item.setText(_translate("Form", "买卖指示"))
        item = self.tableWidget_orders.horizontalHeaderItem(1)
        item.setText(_translate("Form", "代号"))
        item = self.tableWidget_orders.horizontalHeaderItem(2)
        item.setText(_translate("Form", "名称"))
        item = self.tableWidget_orders.horizontalHeaderItem(3)
        item.setText(_translate("Form", "买入余数"))
        item = self.tableWidget_orders.horizontalHeaderItem(4)
        item.setText(_translate("Form", "沽出余数"))
        item = self.tableWidget_orders.horizontalHeaderItem(5)
        item.setText(_translate("Form", "价格"))
        item = self.tableWidget_orders.horizontalHeaderItem(6)
        item.setText(_translate("Form", "有效期"))
        item = self.tableWidget_orders.horizontalHeaderItem(7)
        item.setText(_translate("Form", "条件"))
        item = self.tableWidget_orders.horizontalHeaderItem(8)
        item.setText(_translate("Form", "状况"))
        item = self.tableWidget_orders.horizontalHeaderItem(9)
        item.setText(_translate("Form", "已成交"))
        item = self.tableWidget_orders.horizontalHeaderItem(10)
        item.setText(_translate("Form", "原发者"))
        item = self.tableWidget_orders.horizontalHeaderItem(11)
        item.setText(_translate("Form", "参考"))
        item = self.tableWidget_orders.horizontalHeaderItem(12)
        item.setText(_translate("Form", "时间标记"))
        item = self.tableWidget_orders.horizontalHeaderItem(13)
        item.setText(_translate("Form", "外部指示#"))
        self.tabWidget_acc_info.setTabText(self.tabWidget_acc_info.indexOf(self.tab_orders), _translate("Form", "订单"))
        item = self.tableWidget_pos.horizontalHeaderItem(0)
        item.setText(_translate("Form", "代号"))
        item = self.tableWidget_pos.horizontalHeaderItem(1)
        item.setText(_translate("Form", "名称"))
        item = self.tableWidget_pos.horizontalHeaderItem(2)
        item.setText(_translate("Form", "上日持仓"))
        item = self.tableWidget_pos.horizontalHeaderItem(3)
        item.setText(_translate("Form", "存取"))
        item = self.tableWidget_pos.horizontalHeaderItem(4)
        item.setText(_translate("Form", "今日长仓"))
        item = self.tableWidget_pos.horizontalHeaderItem(5)
        item.setText(_translate("Form", "今日短仓"))
        item = self.tableWidget_pos.horizontalHeaderItem(6)
        item.setText(_translate("Form", "今日净仓"))
        item = self.tableWidget_pos.horizontalHeaderItem(7)
        item.setText(_translate("Form", "净仓"))
        item = self.tableWidget_pos.horizontalHeaderItem(8)
        item.setText(_translate("Form", "市价"))
        item = self.tableWidget_pos.horizontalHeaderItem(9)
        item.setText(_translate("Form", "盈亏"))
        item = self.tableWidget_pos.horizontalHeaderItem(10)
        item.setText(_translate("Form", "前收盘价"))
        item = self.tableWidget_pos.horizontalHeaderItem(11)
        item.setText(_translate("Form", "参考兑换率"))
        item = self.tableWidget_pos.horizontalHeaderItem(12)
        item.setText(_translate("Form", "盈亏"))
        item = self.tableWidget_pos.horizontalHeaderItem(13)
        item.setText(_translate("Form", "合约值"))
        self.tabWidget_acc_info.setTabText(self.tabWidget_acc_info.indexOf(self.tab_pos), _translate("Form", "持仓"))
        item = self.tableWidget_trades.horizontalHeaderItem(0)
        item.setText(_translate("Form", "代号"))
        item = self.tableWidget_trades.horizontalHeaderItem(1)
        item.setText(_translate("Form", "类型"))
        item = self.tableWidget_trades.horizontalHeaderItem(2)
        item.setText(_translate("Form", "名称"))
        item = self.tableWidget_trades.horizontalHeaderItem(3)
        item.setText(_translate("Form", "买入量"))
        item = self.tableWidget_trades.horizontalHeaderItem(4)
        item.setText(_translate("Form", "沽出量"))
        item = self.tableWidget_trades.horizontalHeaderItem(5)
        item.setText(_translate("Form", "成交价"))
        item = self.tableWidget_trades.horizontalHeaderItem(6)
        item.setText(_translate("Form", "成交#"))
        item = self.tableWidget_trades.horizontalHeaderItem(7)
        item.setText(_translate("Form", "状况"))
        item = self.tableWidget_trades.horizontalHeaderItem(8)
        item.setText(_translate("Form", "原发者"))
        item = self.tableWidget_trades.horizontalHeaderItem(9)
        item.setText(_translate("Form", "参考"))
        item = self.tableWidget_trades.horizontalHeaderItem(10)
        item.setText(_translate("Form", "时间"))
        item = self.tableWidget_trades.horizontalHeaderItem(11)
        item.setText(_translate("Form", "指示价"))
        item = self.tableWidget_trades.horizontalHeaderItem(12)
        item.setText(_translate("Form", "指示#"))
        item = self.tableWidget_trades.horizontalHeaderItem(13)
        item.setText(_translate("Form", "成交记录#"))
        self.tabWidget_acc_info.setTabText(self.tabWidget_acc_info.indexOf(self.tab_trades), _translate("Form", "成交结算"))
        item = self.tableWidget_bal.horizontalHeaderItem(0)
        item.setText(_translate("Form", "货币"))
        item = self.tableWidget_bal.horizontalHeaderItem(1)
        item.setText(_translate("Form", "上日结余"))
        item = self.tableWidget_bal.horizontalHeaderItem(2)
        item.setText(_translate("Form", "未交收"))
        item = self.tableWidget_bal.horizontalHeaderItem(3)
        item.setText(_translate("Form", "今日存取"))
        item = self.tableWidget_bal.horizontalHeaderItem(4)
        item.setText(_translate("Form", "现金结余"))
        item = self.tableWidget_bal.horizontalHeaderItem(5)
        item.setText(_translate("Form", "未兑现"))
        item = self.tableWidget_bal.horizontalHeaderItem(6)
        item.setText(_translate("Form", "参考兑换率"))
        item = self.tableWidget_bal.horizontalHeaderItem(7)
        item.setText(_translate("Form", "现金"))
        self.tabWidget_acc_info.setTabText(self.tabWidget_acc_info.indexOf(self.tab_bal), _translate("Form", "现金结余"))
        self.tabWidget_acc_info.setTabText(self.tabWidget_acc_info.indexOf(self.tab_ccy), _translate("Form", "参考汇率"))
