{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "609.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "qMgFqrKQeqa0"
      },
      "source": [
        "class Solution:\n",
        "    def findDuplicate(self, paths: List[str]) -> List[List[str]]:\n",
        "        \n",
        "        a = []\n",
        "        re = dict()\n",
        "        result = []\n",
        "        \n",
        "        for path in paths:\n",
        "            a.append(list(path.split()))\n",
        "            \n",
        "        \n",
        "        for files in a:\n",
        "            directory = files[0]\n",
        "            for file in files[1:]:\n",
        "                filename, content = file.split( '(' )\n",
        "                content = content[:-1]\n",
        "                new_file_path = directory+'/'+filename\n",
        "                if content in re :\n",
        "                    re[content].append(new_file_path)\n",
        "                else:\n",
        "                    re[content] = [new_file_path]\n",
        "                    \n",
        "        for i in re:\n",
        "            if len(re[i]) >1 :\n",
        "                result.append(re[i])\n",
        "            \n",
        "        return result"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
