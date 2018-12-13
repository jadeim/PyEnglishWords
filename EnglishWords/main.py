import MainWindow as MW
import sys

if __name__ == "__main__":
    app = MW.QApplication(sys.argv)
    showWindow = MW.MainWindow()
    sys.exit(app.exec_())