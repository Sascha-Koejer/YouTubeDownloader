/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *action_download_path;
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QLineEdit *urlinput;
    QHBoxLayout *horizontalLayout_2;
    QProgressBar *progressBar;
    QHBoxLayout *horizontalLayout_3;
    QCheckBox *checkBox;
    QPushButton *addbutton;
    QPushButton *downloadbutton;
    QStatusBar *statusbar;
    QMenuBar *menuBar;
    QMenu *menuDatei;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(370, 162);
        MainWindow->setMinimumSize(QSize(0, 0));
        MainWindow->setMaximumSize(QSize(1000, 1000));
        action_download_path = new QAction(MainWindow);
        action_download_path->setObjectName(QString::fromUtf8("action_download_path"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        urlinput = new QLineEdit(centralwidget);
        urlinput->setObjectName(QString::fromUtf8("urlinput"));

        horizontalLayout->addWidget(urlinput);


        gridLayout->addLayout(horizontalLayout, 0, 1, 1, 2);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        progressBar = new QProgressBar(centralwidget);
        progressBar->setObjectName(QString::fromUtf8("progressBar"));
        progressBar->setValue(0);
        progressBar->setTextVisible(true);

        horizontalLayout_2->addWidget(progressBar);


        gridLayout->addLayout(horizontalLayout_2, 2, 1, 1, 2);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        checkBox = new QCheckBox(centralwidget);
        checkBox->setObjectName(QString::fromUtf8("checkBox"));
        checkBox->setLayoutDirection(Qt::LeftToRight);
        checkBox->setTristate(false);

        horizontalLayout_3->addWidget(checkBox);

        addbutton = new QPushButton(centralwidget);
        addbutton->setObjectName(QString::fromUtf8("addbutton"));

        horizontalLayout_3->addWidget(addbutton);

        downloadbutton = new QPushButton(centralwidget);
        downloadbutton->setObjectName(QString::fromUtf8("downloadbutton"));

        horizontalLayout_3->addWidget(downloadbutton);


        gridLayout->addLayout(horizontalLayout_3, 1, 1, 1, 2);

        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 370, 21));
        menuDatei = new QMenu(menuBar);
        menuDatei->setObjectName(QString::fromUtf8("menuDatei"));
        MainWindow->setMenuBar(menuBar);

        menuBar->addAction(menuDatei->menuAction());
        menuDatei->addAction(action_download_path);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "YouTube Downloader", nullptr));
        action_download_path->setText(QApplication::translate("MainWindow", "Dowload Pfad", nullptr));
        urlinput->setPlaceholderText(QApplication::translate("MainWindow", "YouTube Url", nullptr));
        checkBox->setText(QApplication::translate("MainWindow", "Video", nullptr));
        addbutton->setText(QApplication::translate("MainWindow", "Add", nullptr));
        downloadbutton->setText(QApplication::translate("MainWindow", "Download All", nullptr));
        menuDatei->setTitle(QApplication::translate("MainWindow", "Datei", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
